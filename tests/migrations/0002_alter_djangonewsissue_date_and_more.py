# Generated by Django 4.2.4 on 2023-08-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangonewsissue',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='djangonewsissue',
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
