# Generated by Django 4.1.1 on 2023-04-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamleader', '0002_project_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_member',
            name='otp_entered',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team_member',
            name='phone_num',
            field=models.CharField(default='null', max_length=15),
            preserve_default=False,
        ),
    ]