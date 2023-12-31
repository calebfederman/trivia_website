# Generated by Django 4.2.2 on 2023-06-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchup',
            name='ot_loss',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='ot_loss_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='season',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
