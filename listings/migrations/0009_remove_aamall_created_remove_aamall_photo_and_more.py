# Generated by Django 4.1.4 on 2023-04-04 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_remove_image_image_url_image_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aamall',
            name='created',
        ),
        migrations.RemoveField(
            model_name='aamall',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='aamall',
            name='thumbnail_url',
        ),
        migrations.AddField(
            model_name='image',
            name='cats',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.aamall'),
        ),
        migrations.AlterField(
            model_name='aamall',
            name='title',
            field=models.CharField(db_index=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
