# Generated by Django 3.1.4 on 2021-05-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffinfo',
            name='dept',
            field=models.CharField(default='CSE', max_length=100),
        ),
    ]