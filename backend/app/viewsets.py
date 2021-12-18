from django.contrib.auth import get_user_model
from enum import Enum

from django.db.models import Count, F
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Quoter, Quote, Like
from app.serializers import UserSerializer, QuoteSerializer, QuoterSerializer, LikeSerializer, TopQuoterSerializer


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
    queryset = Quote.objects.select_related('quoted_by', 'added_by').all().order_by('-added_at')
    search_fields = ['text', 'quoted_by__name']
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        query_params = request.query_params
        type_param = query_params.get('type', None)
        queryset = self.filter_queryset(self.get_queryset())

        if type_param == QuoteTypeParam.ALL.value:
            queryset = queryset
        elif type_param == QuoteTypeParam.TOP.value:
            queryset = self.filter_queryset(Quote.objects.get_top_quotes())
        else:
            queryset = Quote.objects.filter(added_by__username=request.user)
        quote_ids = queryset.values_list("id", flat=True)
        user_likes = frozenset(Like.objects.filter(quote__in=quote_ids).values_list("quote", flat=True))
        likes_qs = queryset.values("id").annotate(like_count=Count('like'))
        likes_count = {}
        for like in likes_qs:
            likes_count[like['id']] = like['like_count']
        serializer = self.get_serializer(queryset, many=True,
                                         context={"user_likes": user_likes, "likes_count": likes_count})
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


class QuoterTypeParam(Enum):
    TOP = 'top'


class QuoterViewSet(viewsets.ModelViewSet):
    serializer_class = QuoterSerializer
    queryset = Quoter.objects.all()
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]

    def get_serializer_class(self):
        if self.request.query_params.get('type', None):
            return TopQuoterSerializer
        else:
            return QuoterSerializer

    def list(self, request):
        query_params = request.query_params
        type_param = query_params.get('type', None)
        queryset = self.filter_queryset(self.get_queryset())
        likes = {}
        if type_param == QuoterTypeParam.TOP.value:
            likes = Like.objects.annotate(quoter_name=F("quote__quoted_by__name"))
            likes = likes.values("quoter_name").annotate(like_count=Count("quoter_name"))

        queryset = self.filter_queryset(Quoter.objects.get_most_quoted())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={"likes": likes})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={"likes": likes})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def quotes(self, request, pk=None):
        queryset = Quote.objects.get_top_quotes_by_quoter_with_id(pk)
        serializer = QuoteSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def create(self, request, *args, **kwargs):
        like = Like.objects.filter(quote=request.data["quote"], user=request.user).first()
        if like:
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer_data = {"quote": request.data["quote"], "user": request.user.id}
            serializer = self.get_serializer(data=serializer_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({"errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
