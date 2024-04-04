# Generated by Django 4.2.10 on 2024-02-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('address', models.CharField(max_length=256, verbose_name='Адресс')),
                ('website', models.CharField(max_length=256, verbose_name='Веб-сайт')),
                ('phone', models.CharField(max_length=32, verbose_name='Телефон')),
                ('specialization', models.ManyToManyField(to='web.specialization', verbose_name='Специализация')),
            ],
        ),
    ]
