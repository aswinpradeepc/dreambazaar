# Generated by Django 4.2.2 on 2023-09-24 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemsforsale',
            old_name='department',
            new_name='category',
        ),
    ]