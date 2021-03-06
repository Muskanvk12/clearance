# Generated by Django 3.1.4 on 2021-05-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_accountsection_artificialintelligence_computernetwork_functionalenglish_hod_library_sepm'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountsection',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artificialintelligence',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='computernetwork',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designpattern',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='functionalenglish',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hod',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='library',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sepm',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
