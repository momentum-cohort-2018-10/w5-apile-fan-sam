# Generated by Django 2.0 on 2018-11-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.BooleanField(),
        ),
    ]
