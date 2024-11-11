# Generated by Django 5.0.2 on 2024-11-11 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbusers', '0002_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='title',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='caption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='gallery_images/'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='gallery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dbusers.gallery'),
        ),
    ]