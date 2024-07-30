# Generated by Django 5.0.7 on 2024-07-30 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenario', '0003_remove_scenario_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=20)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenario.scenario')),
            ],
        ),
    ]
