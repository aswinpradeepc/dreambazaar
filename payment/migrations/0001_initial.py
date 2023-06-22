# Generated by Django 4.2.2 on 2023-06-22 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_shop', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_payment_id', models.CharField(max_length=255)),
                ('razorpay_order_id', models.CharField(max_length=255)),
                ('razorpay_signature', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending', max_length=255)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shop.order')),
            ],
        ),
    ]
