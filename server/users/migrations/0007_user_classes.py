# Generated by Django 3.1.3 on 2020-12-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201212_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='classes',
            field=models.CharField(blank=True, default='', max_length=8096),
        ),
    ]
