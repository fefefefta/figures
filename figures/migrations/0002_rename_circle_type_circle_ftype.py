# Generated by Django 4.0.1 on 2022-01-29 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='circle',
            old_name='circle_type',
            new_name='ftype',
        ),
    ]