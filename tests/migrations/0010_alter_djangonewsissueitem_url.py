# Generated by Django 4.2.4 on 2023-08-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_djangonewsissueitem_url_status_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangonewsissueitem',
            name='url',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
