# Generated by Django 4.2.4 on 2023-09-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]