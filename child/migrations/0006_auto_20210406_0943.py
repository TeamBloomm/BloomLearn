# Generated by Django 3.0.5 on 2021-04-06 06:43

import child.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0003_auto_20210406_0943'),
        ('child', '0005_auto_20210403_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='childdata',
            name='Courses',
            field=djongo.models.fields.ArrayReferenceField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='teacher.CourseData'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childdata',
            name='subjects',
            field=djongo.models.fields.ArrayField(default=django.utils.timezone.now, model_container=child.models.Subject),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='childdata',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
    ]
