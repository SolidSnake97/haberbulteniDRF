# Generated by Django 4.1.6 on 2023-02-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_makale_yazar'),
    ]

    operations = [
        migrations.AddField(
            model_name='gazeteci',
            name='biografy',
            field=models.TextField(blank=True, null=True),
        ),
    ]