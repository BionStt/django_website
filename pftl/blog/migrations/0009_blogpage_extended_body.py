# Generated by Django 3.0.5 on 2020-05-31 14:46

from django.db import migrations
import pftl.blog.blocks
import wagtail.core.fields
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191223_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='extended_body',
            field=wagtail.core.fields.StreamField([('content', wagtailmarkdown.blocks.MarkdownBlock()), ('newsletter', pftl.blog.blocks.NewsletterSubscribe())], null=True),
        ),
    ]
