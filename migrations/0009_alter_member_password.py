# Generated by Django 5.0 on 2024-01-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_member_identifiant_alter_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
