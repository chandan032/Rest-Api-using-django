# Generated by Django 3.0.8 on 2021-10-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=60)),
                ('job_description', models.TextField()),
                ('salary', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=35)),
                ('state', models.CharField(max_length=35)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
