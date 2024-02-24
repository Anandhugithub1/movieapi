# Generated by Django 5.0 on 2024-02-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
        migrations.AddField(
            model_name='movie',
            name='revenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
