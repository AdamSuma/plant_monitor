# Generated by Django 2.2.1 on 2019-05-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190517_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.IntegerField()),
                ('hum_soil', models.IntegerField()),
                ('hum_air', models.IntegerField()),
                ('light', models.IntegerField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Sensor')),
            ],
        ),
    ]
