# Generated by Django 3.1.3 on 2020-12-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qualification',
            field=models.CharField(blank=True, default='Student', max_length=40),
        ),
    ]
