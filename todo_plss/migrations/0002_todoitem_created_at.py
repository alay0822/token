# Generated by Django 5.1.6 on 2025-04-04 04:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_plss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
