# Generated by Django 4.0.2 on 2022-03-30 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('name', models.CharField(max_length=256, verbose_name='姓名')),
                ('email', models.CharField(max_length=256, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=256, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=256, verbose_name='年龄')),
                ('sector', models.CharField(max_length=256, verbose_name='科室')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='姓名')),
            ],
            options={
                'verbose_name': '医生',
                'verbose_name_plural': '医生',
            },
        ),
    ]
