# Generated by Django 5.0.6 on 2024-06-30 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_events_cost_remove_venue_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='events',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='events',
            name='start_date',
        ),
    ]
