# Generated by Django 4.1.4 on 2023-04-08 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_remove_aamall_created_remove_aamall_photo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aamall',
            old_name='category',
            new_name='cat_id',
        ),
    ]
