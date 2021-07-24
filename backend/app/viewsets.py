from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Quoter, Quote
from app.serializers import UserSerializer, QuoteSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    UserModel = get_user_model()
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


def _create_quote_and_save(quote, quoter, added_by):
    new_quote = Quote(text=quote, quoted_by=quoter, added_by=added_by)
    new_quote.save()
    return new_quote


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Quote.objects.filter(added_by__username=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        print(request.data)
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
