# Generated by Django 4.1.2 on 2022-10-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_applications_delete_activationlinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Принято'),
        ),
    ]
