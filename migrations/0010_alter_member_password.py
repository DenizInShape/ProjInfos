# Generated by Django 5.0 on 2024-01-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_member_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
