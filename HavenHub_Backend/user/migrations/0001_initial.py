# Generated by Django 4.2.5 on 2024-04-21 21:16

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200)),
                ('profile_picture', models.ImageField(blank=True, height_field='heigth_length', null=True, upload_to=user.models.uploaded_to, width_field='width_length')),
                ('id_picture', models.ImageField(blank=True, height_field='heigth_length', null=True, upload_to=user.models.id_uploaded_to, width_field='width_length')),
                ('width_length', models.IntegerField(blank=True, default=0, null=True)),
                ('heigth_length', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
