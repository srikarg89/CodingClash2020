# Generated by Django 3.0.5 on 2020-07-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='secret',
            field=models.CharField(default='hello', max_length=16),
            preserve_default=False,
        ),
    ]