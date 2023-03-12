# Generated by Django 4.1.4 on 2023-03-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_rename_image_aamall_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='aamall',
            name='photo',
            field=models.FileField(default=1, upload_to='photo_data'),
            preserve_default=False,
        ),
    ]