from datetime import datetime

from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models import Count


class QuoterManager(models.Manager):
    def get_most_quoted(self):
        return self.values(
            "id", "name", "added_by"
        ).annotate(
            quote_count=Count("quotes")
        ).filter(
            quote_count__gt=0
        ).order_by(
            "-quote_count"
        )


class Quoter(models.Model):
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    objects = QuoterManager()


class QuoteManager(models.Manager):
    # Returns the most liked quotes
    def get_top_quotes(self):
        return self.annotate(likes=Count('like')).order_by('-likes', '-added_at')

    def get_top_quotes_by_quoter_with_id(self, quoter_id):
        return self.filter(quoted_by__id=quoter_id).annotate(likes=Count('like')).order_by('-likes', "-added_at")[:3]

    def search_for_quotes(self, search_text):
        return self.filter(text__icontains=search_text, quoted_by__name__icontains=search_text)


class Quote(models.Model):
    text = models.CharField(max_length=1000)
    quoted_by = models.ForeignKey(Quoter, on_delete=models.CASCADE, related_name="quotes")
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
