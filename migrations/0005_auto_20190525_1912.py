# Generated by Django 2.1.7 on 2019-05-25 11:12

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_library', '0004_auto_20190525_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
    ]
