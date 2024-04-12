# Generated by Django 5.0.4 on 2024-04-12 05:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_customuser_college_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hours', models.IntegerField()),
                ('teacher', models.ForeignKey(limit_choices_to={'status': 'Teacher'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='homework/')),
                ('Title', models.CharField(blank=True, max_length=20, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('StudentComment', models.TextField(blank=True, null=True)),
                ('Mark', models.IntegerField(blank=True, null=True)),
                ('homework', models.FileField(blank=True, null=True, upload_to='homework')),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
