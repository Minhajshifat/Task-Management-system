# Generated by Django 5.0 on 2024-01-04 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_taskmodel_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='is_complete',
            new_name='complete',
        ),
    ]
