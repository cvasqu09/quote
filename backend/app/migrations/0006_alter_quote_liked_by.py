# Generated by Django 3.2.3 on 2021-11-11 18:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_quote_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='liked_by',
            field=models.ManyToManyField(default=None, related_name='liked_quotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
