# Generated by Django 3.0.3 on 2020-02-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
