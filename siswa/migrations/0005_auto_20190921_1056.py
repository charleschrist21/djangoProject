# Generated by Django 2.2.3 on 2019-09-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0004_auto_20190921_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='tanggal_lahir',
            field=models.IntegerField(default=0),
        ),
    ]
