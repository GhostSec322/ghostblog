# Generated by Django 5.1.4 on 2025-01-15 11:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_content_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
