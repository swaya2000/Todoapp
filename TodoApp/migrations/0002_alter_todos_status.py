# Generated by Django 5.0.7 on 2024-07-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
