# Generated by Django 3.2.25 on 2024-04-17 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('request_adopt', '0002_alter_requestadopt_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestadopt',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile'),
        ),
    ]
