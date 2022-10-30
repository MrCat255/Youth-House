# Generated by Django 4.1.2 on 2022-10-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_applications_accepted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applications',
            options={'verbose_name': 'Заявку', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='applications',
            name='accepted',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Принято'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='hall',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер зала'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='tel',
            field=models.TextField(blank=True, null=True, verbose_name='Tel'),
        ),
    ]
