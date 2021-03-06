# Generated by Django 3.1.5 on 2021-01-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210123_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='firstname',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='lastname',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='username',
        ),
        migrations.AddField(
            model_name='provider',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='provider',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='provider',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='provider',
            name='pincode',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='provider',
            name='state',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
