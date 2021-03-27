# Generated by Django 3.0.5 on 2021-03-25 22:08

import child.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import djongo.models.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_user', models.CharField(max_length=500)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('guardian', djongo.models.fields.EmbeddedField(model_container=child.models.Guardian)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
