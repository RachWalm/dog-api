# Generated by Django 3.2.24 on 2024-04-24 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dog_profile', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourited', to='dog_profile.dogprofile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='user_profile.userprofile')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user_id', 'dog_id')},
            },
        ),
    ]
