# Generated by Django 5.0.3 on 2024-04-02 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.question'),
        ),
    ]
