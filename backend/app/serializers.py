from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.models import Quote, Quoter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        UserModel = get_user_model()
        model = UserModel
        fields = ['username']


class QuoteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='added_by.username', read_only=True)
    quoter = serializers.CharField(source='quoted_by.name', read_only=True)

    class Meta:
        model = Quote
        fields = ['id', 'text', 'username', 'quoter']


class QuoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quoter
        fields = '__all__'
