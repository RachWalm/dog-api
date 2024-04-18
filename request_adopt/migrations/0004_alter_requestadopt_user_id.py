# Generated by Django 3.2.25 on 2024-04-17 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request_adopt', '0003_alter_requestadopt_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestadopt',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]