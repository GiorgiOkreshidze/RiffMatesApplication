# Generated by Django 5.1.4 on 2024-12-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bands', '0002_venue_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('musicians', models.ManyToManyField(to='Bands.musician')),
            ],
        ),
    ]
