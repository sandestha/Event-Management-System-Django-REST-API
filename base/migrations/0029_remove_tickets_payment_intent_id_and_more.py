# Generated by Django 5.0.6 on 2024-07-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_tickets_payment_intent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='payment_intent_id',
        ),
        migrations.AddField(
            model_name='tickets',
            name='payment_method',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='ticket_no',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
