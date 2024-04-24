# Generated by Django 3.2.24 on 2024-04-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('received_date', models.DateField(blank=True, null=True)),
                ('rehomed_date', models.DateField(blank=True, null=True)),
                ('returned_date', models.DateField(blank=True, null=True)),
                ('dog_age', models.IntegerField(blank=True)),
                ('dog_breed', models.CharField(max_length=255)),
                ('dog_gender', models.IntegerField(choices=[(0, 'TBC'), (1, 'Male'), (2, 'Female')], default=0)),
                ('dog_size', models.IntegerField(choices=[(0, 'TBC'), (1, 'Small'), (2, 'Large')], default=0)),
                ('dog_image', models.ImageField(default='../dog-image-na_zmmfot', upload_to='images/')),
                ('at_rescue', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(0, 'To arrive'), (1, 'Not available'), (2, 'Available'), (3, 'Rehomed')], default=0)),
                ('general', models.TextField()),
                ('home_cats', models.BooleanField(default=False)),
                ('home_dogs', models.BooleanField(default=False)),
                ('home_animals', models.BooleanField(default=False)),
                ('home_children', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GenderChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SizeChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StatusChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
