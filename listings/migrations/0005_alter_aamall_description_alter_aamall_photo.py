# Generated by Django 4.1.4 on 2023-01-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_aamall_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aamall',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aamall',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
