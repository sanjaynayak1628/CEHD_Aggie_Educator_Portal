# Generated by Django 4.0.3 on 2022-04-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_logs', '0003_alter_timelogs_hours_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelogs',
            name='semester_year',
            field=models.CharField(default=2022, max_length=4),
            preserve_default=False,
        ),
    ]
