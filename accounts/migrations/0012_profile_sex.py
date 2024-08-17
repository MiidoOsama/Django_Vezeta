# Generated by Django 5.1 on 2024-08-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_profile_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=50, verbose_name='النوع'),
            preserve_default=False,
        ),
    ]
