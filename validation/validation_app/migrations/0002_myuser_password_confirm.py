# Generated by Django 4.2.14 on 2024-07-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='password_confirm',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
