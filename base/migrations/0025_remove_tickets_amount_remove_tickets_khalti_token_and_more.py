# Generated by Django 5.0.6 on 2024-07-05 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_tickets_amount_tickets_khalti_token_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='khalti_token',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='purchase_date',
        ),
    ]
