# Generated by Django 3.0.3 on 2020-02-29 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=1000)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2020, 2, 29, 16, 58, 41, 289604))),
            ],
        ),
    ]
