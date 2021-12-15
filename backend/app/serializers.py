from datetime import datetime

from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.models import Quote, Quoter, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        UserModel = get_user_model()
        model = UserModel
        fields = ['username']


class QuoteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='added_by.username', read_only=True)
    quoter = serializers.CharField(source='quoted_by.name', read_only=True)
    liked_by_user = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_liked_by_user(self, obj):
        # print('user_likes', self.context)
        return obj.id in self.context.get("user_likes", [])

    def get_like_count(self, obj):
        # print('self.context', self.context["likes_count"])
        likes_count = self.context.get("likes_count", {})
        return likes_count.get(obj.id, 0)

    class Meta:
        model = Quote
        fields = ['id', 'text', 'username', 'quoter', 'liked_by_user', 'like_count']


class QuoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quoter
        fields = ["id", "name"]


class LikeSerializer(serializers.ModelSerializer):
    liked_at = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = Like
        fields = '__all__'
