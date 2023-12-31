# Generated by Django 4.2.4 on 2023-08-22 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('car_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.car')),
                ('bed_length', models.IntegerField(default=5)),
            ],
            options={
                'ordering': ['make', 'year'],
                'abstract': False,
            },
            bases=('main_app.car',),
        ),
    ]
