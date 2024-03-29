# Generated by Django 4.1.4 on 2023-04-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_aamall_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aamall',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='aamall',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='aamall',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
