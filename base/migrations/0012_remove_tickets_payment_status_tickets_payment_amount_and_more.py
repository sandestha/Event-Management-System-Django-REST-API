# Generated by Django 5.0.6 on 2024-06-29 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_venue_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='tickets',
            name='payment_amount',
            field=models.IntegerField(blank=True, null=True),
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
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
