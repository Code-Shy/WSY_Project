# Generated by Django 4.0.2 on 2022-03-23 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_alter_storage_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(default=0.0, verbose_name='金额/(元)')),
                ('type', models.CharField(max_length=64, verbose_name='类型')),
                ('datatime', models.DateTimeField(max_length=19, verbose_name='时间')),
                ('purpose', models.CharField(max_length=256, verbose_name='用途')),
                ('remark', models.CharField(max_length=256, verbose_name='备注')),
            ],
            options={
                'verbose_name': '收支管理',
                'verbose_name_plural': '收支管理',
            },
        ),
    ]
