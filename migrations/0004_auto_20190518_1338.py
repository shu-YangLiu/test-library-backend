# Generated by Django 2.1.7 on 2019-05-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_library', '0003_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, default='null', max_length=50, null=True, verbose_name='A'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, default='null', max_length=50, null=True, verbose_name='B'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, default='null', max_length=50, null=True, verbose_name='C'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, default='null', max_length=50, null=True, verbose_name='D'),
        ),
    ]
