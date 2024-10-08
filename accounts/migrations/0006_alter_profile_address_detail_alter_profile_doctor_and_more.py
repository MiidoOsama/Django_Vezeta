# Generated by Django 5.1 on 2024-08-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_address_profile_address_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(max_length=80, verbose_name='العنوان '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(max_length=50, verbose_name='دكتور'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=500, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number_phone',
            field=models.CharField(max_length=20, verbose_name='رقم التليفون  '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الكشف '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='specialist_doctor',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='التخصص  '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='waiting_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='مدة الانتظار'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='who_i',
            field=models.TextField(max_length=50, verbose_name='من انا '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='working_hours',
            field=models.IntegerField(verbose_name='ساعات العمل '),
        ),
    ]
