# Generated by Django 2.1.1 on 2019-07-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_auto_20190717_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='_id',
            field=models.IntegerField(default=2036),
        ),
    ]
