# Generated by Django 3.0.6 on 2020-06-03 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benpelumiscrumy', '0009_auto_20200603_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_id',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]