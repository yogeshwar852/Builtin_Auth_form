# Generated by Django 2.2.7 on 2020-06-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0003_auto_20200604_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='mobile',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
