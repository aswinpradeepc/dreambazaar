# Generated by Django 4.2.2 on 2023-06-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookforsale',
            name='preview_3',
            field=models.ImageField(blank=True, null=True, upload_to='book_images'),
        ),
    ]