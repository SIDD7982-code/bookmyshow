# Generated by Django 4.0.3 on 2024-01-21 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_alter_movietime_show_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.AddField(
            model_name='movierating',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.movie'),
        ),
    ]
