# Generated by Django 3.2.23 on 2024-01-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0097_remove_recentaction_old_model_affected'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='mortgage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
