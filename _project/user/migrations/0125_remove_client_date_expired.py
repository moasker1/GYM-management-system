# Generated by Django 3.2.23 on 2024-04-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0124_client_date_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_expired',
        ),
    ]
