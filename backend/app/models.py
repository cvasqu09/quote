from django.conf import settings
from django.db import models

# Create your models here.
class Quoter(models.Model):
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

class Quote(models.Model):
    text = models.CharField(max_length=1000)
    quoted_by = models.ForeignKey(Quoter, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_quotes", default=None)
    added_at = models.DateTimeField()

