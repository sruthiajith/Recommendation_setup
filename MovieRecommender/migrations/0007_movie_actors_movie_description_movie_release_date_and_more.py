# Generated by Django 4.2.11 on 2024-03-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieRecommender', '0006_delete_detailes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.CharField(max_length=750, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer_link',
            field=models.URLField(max_length=250, null=True, unique=True),
        ),
    ]
