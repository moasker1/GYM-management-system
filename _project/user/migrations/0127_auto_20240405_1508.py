# Generated by Django 3.2.23 on 2024-04-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0126_auto_20240405_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='client',
        ),
        migrations.AddField(
            model_name='payment',
            name='lose',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
