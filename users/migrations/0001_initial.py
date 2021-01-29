# Generated by Django 3.1.5 on 2021-01-23 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField(default=456)),
                ('mobile', models.CharField(default='Meet', max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_time_login', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50)),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
