# Generated by Django 4.0.1 on 2022-01-21 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('td', '0003_alter_allusers_date_created_alter_allusers_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusers',
            name='username',
            field=models.CharField(max_length=500),
        ),
    ]
