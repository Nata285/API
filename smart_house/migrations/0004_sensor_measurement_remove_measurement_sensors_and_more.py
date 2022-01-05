# Generated by Django 4.0 on 2022-01-05 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_house', '0003_measurement_delete_measurements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='sensors',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensors',
            field=models.ManyToManyField(related_name='measurements', through='smart_house.Sensor_Measurement', to='smart_house.Sensor'),
        ),
        migrations.AddField(
            model_name='sensor_measurement',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='smart_house.measurement'),
        ),
        migrations.AddField(
            model_name='sensor_measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='smart_house.sensor'),
        ),
    ]
