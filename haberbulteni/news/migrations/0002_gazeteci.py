# Generated by Django 4.1.6 on 2023-02-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gazeteci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=150)),
                ('soyisim', models.CharField(max_length=150)),
            ],
        ),
    ]