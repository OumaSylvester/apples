# Generated by Django 4.2.1 on 2023-06-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_production', models.DateField()),
                ('breed', models.CharField(max_length=100)),
                ('row', models.IntegerField()),
                ('column', models.IntegerField(max_length=100)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
    ]