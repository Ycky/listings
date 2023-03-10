# Generated by Django 4.1.4 on 2022-12-22 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AAMAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('city', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image')),
                ('image_url', models.URLField(blank=True, max_length=234, null=True)),
                ('adl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='listings.aamall')),
            ],
        ),
    ]
