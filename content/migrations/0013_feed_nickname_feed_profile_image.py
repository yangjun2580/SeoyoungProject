# Generated by Django 4.1.7 on 2023-10-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_bookmark_feed_like_reply_delete_contentbookmark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='nickname',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='profile_image',
            field=models.TextField(null=True),
        ),
    ]
