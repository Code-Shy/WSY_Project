# Generated by Django 4.0.2 on 2022-03-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default=None, max_length=256, verbose_name='密码'),
        ),
    ]