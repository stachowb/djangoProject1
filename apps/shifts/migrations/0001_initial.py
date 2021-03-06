# Generated by Django 3.2.5 on 2021-07-19 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=10)),
                ('clock_in', models.CharField(max_length=120)),
                ('clock_out', models.CharField(max_length=120)),
                ('distance', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver')),
            ],
        ),
    ]
