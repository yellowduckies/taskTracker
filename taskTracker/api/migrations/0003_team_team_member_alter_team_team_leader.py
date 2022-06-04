# Generated by Django 4.0.5 on 2022-06-04 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_team_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_member',
            field=models.ManyToManyField(related_name='tm', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tl', to=settings.AUTH_USER_MODEL),
        ),
    ]