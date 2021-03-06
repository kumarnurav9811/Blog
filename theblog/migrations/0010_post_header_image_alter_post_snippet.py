# Generated by Django 4.0 on 2021-12-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
