# Generated by Django 3.2.23 on 2024-01-15 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0067_auto_20240115_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense_type', models.CharField(default='غير معروف', max_length=30)),
                ('expense_notes', models.CharField(max_length=50)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.container')),
            ],
        ),
    ]
