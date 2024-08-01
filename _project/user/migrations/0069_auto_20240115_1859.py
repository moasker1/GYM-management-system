# Generated by Django 3.2.23 on 2024-01-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0068_containerexpense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='temp_rest',
        ),
        migrations.AddField(
            model_name='payment',
            name='rest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
