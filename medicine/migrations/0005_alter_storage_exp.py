# Generated by Django 4.0.2 on 2022-03-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_alter_storage_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='exp',
            field=models.IntegerField(default=3, verbose_name='保质期/年'),
        ),
    ]