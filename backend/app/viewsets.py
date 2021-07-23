from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Quoter
from app.serializers import UserSerializer, QuoteSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    UserModel = get_user_model()
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        request_name = request.data["name"]
        print(request_name)
        print(request.user)
        quoter = Quoter.objects.filter(name=request_name)

        # # Create new quoter if not found
        # if len(quoter) == 0:
        #     new_quoter = Quote(name=request_name, added)

        return Response("", status=status.HTTP_201_CREATED)