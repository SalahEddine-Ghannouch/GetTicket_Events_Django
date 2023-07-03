# Generated by Django 2.2.28 on 2023-05-31 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='uid',
        ),
        migrations.AlterField(
            model_name='event',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Ticket'),
        ),
    ]
