# Generated by Django 4.2.3 on 2023-07-14 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('REHOBOTH', 'REHOBOTH'), ('NEW MALE', 'NEW MALE'), ('VICTORY', 'VICTORY'), ('FAITH', 'FAITH'), ('BISHOP', 'BISHOP')], max_length=125)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('total_rooms', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.PositiveIntegerField()),
                ('space_available', models.PositiveIntegerField(default=6)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('matric_no', models.CharField(max_length=30)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
