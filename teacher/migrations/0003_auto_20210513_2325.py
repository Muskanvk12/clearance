# Generated by Django 3.1.4 on 2021-05-13 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_staffinfo_dept'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffinfo',
            options={'ordering': ['id']},
        ),
    ]
