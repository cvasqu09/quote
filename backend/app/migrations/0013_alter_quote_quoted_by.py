# Generated by Django 3.2.3 on 2021-12-15 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_like_liked_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quoted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='app.quoter'),
        ),
    ]
