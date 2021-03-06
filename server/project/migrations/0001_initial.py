# Generated by Django 3.1.3 on 2020-12-12 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1024)),
                ('type', models.CharField(choices=[('DOC', 'Document'), ('COD', 'Code')], default='DOC', max_length=3)),
                ('status', models.CharField(choices=[('STD', 'Started'), ('WRK', 'Working'), ('SUB', 'Submitted'), ('EVL', 'Evaluated')], default='STD', max_length=3)),
                ('grade', models.CharField(blank=True, default='0.00', max_length=3)),
                ('github_link', models.CharField(blank=True, default='', max_length=1024)),
                ('assigned_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_class', to=settings.AUTH_USER_MODEL)),
                ('assigned_mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_mentor', to=settings.AUTH_USER_MODEL)),
                ('assigned_student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
