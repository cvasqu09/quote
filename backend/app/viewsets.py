from django.contrib.auth import get_user_model
from enum import Enum
from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Quoter, Quote
from app.serializers import UserSerializer, QuoteSerializer, QuoterSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    UserModel = get_user_model()
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


def _create_quote_and_save(quote, quoter, added_by):
    new_quote = Quote(text=quote, quoted_by=quoter, added_by=added_by)
    new_quote.save()
    return new_quote


class QuoteTypeParam(Enum):
    ALL = 'all'
    TOP = 'top'

class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all().order_by('-added_at')

    def list(self, request):
        query_params = request.query_params
        type_param = query_params.get('type', None)
        print(type_param)
        if type_param == QuoteTypeParam.ALL.value:
            queryset = self.queryset
        elif type_param == QuoteTypeParam.TOP.value:
            # TODO: Use Top quotes
            queryset = self.queryset
        else:
            queryset = Quote.objects.filter(added_by__username=request.user)
        print('liked by', queryset.first().liked_by.all())
        print('liked by', queryset.first().id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        quoter_name = request.data["name"]
        quote = request.data["text"]
        user = request.user

        quoter = Quoter.objects.filter(name=quoter_name)

        # Create new quoter if not found
        if len(quoter) == 0:
            new_quoter = Quoter(name=quoter_name, added_by=user)
            new_quoter.save()
            new_quote = _create_quote_and_save(quote, new_quoter, user)
        else:
            new_quote = _create_quote_and_save(quote, quoter.first(), user)

        serializer = self.get_serializer(new_quote)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuoterViewSet(viewsets.ModelViewSet):
    serializer_class = QuoterSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Quoter.objects.all()
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]
