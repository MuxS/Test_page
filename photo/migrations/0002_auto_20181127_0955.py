# Generated by Django 2.1.3 on 2018-11-27 00:55

from django.db import migrations
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m'),
        ),
    ]
