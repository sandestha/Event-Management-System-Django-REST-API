# Generated by Django 5.0.6 on 2024-07-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_remove_tickets_amount_remove_tickets_khalti_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='payment_method',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]