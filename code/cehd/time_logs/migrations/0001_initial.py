# Generated by Django 4.0.3 on 2022-04-04 07:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.EmailField(max_length=254)),
                ('log_date', models.DateField()),
                ('notes', models.TextField(default='')),
                ('hours_submitted', models.PositiveIntegerField(default=0)),
                ('hours_approved', models.BooleanField()),
                ('approval_due_date', models.DateField()),
                ('semester', models.CharField(max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('date_submitted', models.DateField(default=datetime.date.today)),
                ('student_uin', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='person_uin', to='core.person', to_field='uin')),
            ],
            options={
                'db_table': 'time_logs',
            },
        ),
    ]
