# Generated by Django 4.2.7 on 2023-11-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
