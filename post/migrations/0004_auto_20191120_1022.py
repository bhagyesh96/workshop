# Generated by Django 2.2.7 on 2019-11-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20191120_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='postdetail',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
