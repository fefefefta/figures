# Generated by Django 4.0.1 on 2022-02-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0003_circle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='image',
            field=models.ImageField(default='figures/Круг.png', upload_to='figures/'),
        ),
    ]