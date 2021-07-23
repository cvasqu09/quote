from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.models import Quote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        UserModel = get_user_model()
        model = UserModel
        fields = ['username']


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'