# Generated by Django 3.0.5 on 2020-05-18 06:23

import codingclash.apps.games.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('submitted_time', models.DateTimeField(auto_now=True)),
                ('code', models.FileField(default=None, upload_to=codingclash.apps.games.models._code_save_path)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished', models.BooleanField(default=False)),
                ('replay', models.FileField(blank=True, upload_to=codingclash.apps.games.models._replay_save_path)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('blue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blue', to='games.Submission')),
                ('outcome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outcome', to='games.Submission')),
                ('red', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='red', to='games.Submission')),
            ],
        ),
    ]
