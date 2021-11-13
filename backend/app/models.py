from datetime import datetime

from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models import Count


class Quoter(models.Model):
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)


class QuoteManager(models.Manager):
    def get_top_quotes(self):
        return self.annotate(likes=Count('like')).order_by('-likes', '-added_at')


class Quote(models.Model):
    text = models.CharField(max_length=1000)
    quoted_by = models.ForeignKey(Quoter, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    objects = QuoteManager()


class LikesManager(models.Manager):
    def get_likes_by_user(self, user):
        return self.filter(user=user)

    def get_like_count(self, quote):
        return self.filter(quote=quote).count()


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="like")
    liked_at = models.DateTimeField(auto_now_add=True)
    objects = LikesManager()
