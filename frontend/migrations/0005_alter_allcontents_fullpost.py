# Generated by Django 3.2.13 on 2023-06-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_allposts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcontents',
            name='fullpost',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
    ]