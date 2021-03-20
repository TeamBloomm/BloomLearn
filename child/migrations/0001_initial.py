# Generated by Django 3.0.5 on 2021-03-20 17:45

import child.models
import django.core.validators
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('first_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email_address', models.EmailField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('repeat_pass', models.CharField(max_length=20)),
                ('guardian', djongo.models.fields.EmbeddedField(model_container=child.models.Guardian)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]