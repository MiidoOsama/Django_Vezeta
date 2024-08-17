# Generated by Django 5.1 on 2024-08-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_profile_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(default=1, max_length=50, verbose_name='اللقب'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=80, verbose_name='الاسم'),
        ),
    ]
