# Generated by Django 5.1 on 2024-08-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_profile_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت الانضمام '),
        ),
    ]
