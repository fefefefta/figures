# Generated by Django 4.0.1 on 2022-02-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0007_alter_circle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='image',
            field=models.ImageField(default='figures/Круг1.png', upload_to='figures/'),
        ),
    ]
