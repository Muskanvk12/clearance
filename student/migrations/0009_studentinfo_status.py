# Generated by Django 3.1.4 on 2021-05-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_studentinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]