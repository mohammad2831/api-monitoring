# Generated by Django 5.2.4 on 2025-07-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.CharField(max_length=500)),
                ('interval_minutes', models.IntegerField(default=1)),
            ],
        ),
    ]
