# Generated by Django 3.0.5 on 2021-04-03 17:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('child', '0001_initial'),
        ('teacher', '0002_auto_20210403_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='timeSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('slotDate', models.DateField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.TeacherData')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('sessionDate', models.DateTimeField()),
                ('isConfirmed', models.BooleanField()),
                ('isRejected', models.BooleanField()),
                ('isCompleted', models.BooleanField()),
                ('sessionUrl', models.URLField()),
                ('sessionID', models.CharField(max_length=100)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('appointmentWith', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='child.ChildData')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.TeacherData')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
