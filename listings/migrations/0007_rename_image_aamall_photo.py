# Generated by Django 4.1.4 on 2023-02-28 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_remove_aamall_photo_aamall_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aamall',
            old_name='image',
            new_name='photo',
        ),
    ]