# Generated by Django 3.0.6 on 2020-06-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benpelumiscrumy', '0008_auto_20200603_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_id',
            field=models.IntegerField(default=3045, null=True, unique=True),
        ),
    ]