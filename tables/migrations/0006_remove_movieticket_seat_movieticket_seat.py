# Generated by Django 4.2.9 on 2024-02-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_movieticket_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieticket',
            name='seat',
        ),
        migrations.AddField(
            model_name='movieticket',
            name='seat',
            field=models.ManyToManyField(to='tables.movieseats'),
        ),
    ]