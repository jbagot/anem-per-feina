# Generated by Django 3.0.7 on 2020-11-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0014_auto_20201103_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.PositiveIntegerField(blank=True, default=None, help_text='Minimum and maximum annual salary for this job.', null=True, verbose_name='Salary'),
        ),
    ]