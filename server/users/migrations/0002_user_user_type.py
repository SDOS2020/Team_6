# Generated by Django 3.1.3 on 2020-11-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('MN', 'Mentor'), ('ME', 'Mentee')], default='ME', max_length=3),
        ),
    ]