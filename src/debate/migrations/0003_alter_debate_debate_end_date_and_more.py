# Generated by Django 4.0.7 on 2022-08-18 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0002_debateactor_actor_team_alter_debate_debate_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='debate_end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 20, 13, 51, 163517)),
        ),
        migrations.AlterField(
            model_name='debate',
            name='debate_start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 17, 13, 51, 163517)),
        ),
    ]