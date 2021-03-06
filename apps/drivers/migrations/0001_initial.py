# Generated by Django 3.2.5 on 2021-07-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0002_company_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('vehicle', models.IntegerField(choices=[(1, 'Trekker'), (2, 'Containerbil m/løftelem'), (3, 'Containerbil'), (4, '-')])),
                ('slug', models.SlugField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
        ),
    ]
