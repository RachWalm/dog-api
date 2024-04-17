# Generated by Django 3.2.25 on 2024-04-17 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dog_profile', '0003_auto_20240416_1634'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestAdopt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_permission', models.BooleanField(default=False)),
                ('home_children', models.BooleanField(default=False)),
                ('home_cats', models.BooleanField(default=False)),
                ('home_animals', models.BooleanField(default=False)),
                ('home_dogs', models.BooleanField(default=False)),
                ('experience', models.TextField(blank=True, max_length=1000, null=True)),
                ('query', models.TextField(blank=True, max_length=1000, null=True)),
                ('dog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dog_profile.dogprofile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]