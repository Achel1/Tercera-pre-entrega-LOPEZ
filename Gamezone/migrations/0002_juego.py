# Generated by Django 5.1 on 2024-08-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamezone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
    ]
