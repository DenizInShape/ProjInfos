# Generated by Django 5.0 on 2024-01-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
