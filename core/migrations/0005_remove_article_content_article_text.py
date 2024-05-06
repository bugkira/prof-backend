# Generated by Django 5.0.4 on 2024-05-04 09:38

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_section_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="content",
        ),
        migrations.AddField(
            model_name="article",
            name="text",
            field=django_ckeditor_5.fields.CKEditor5Field(
                default="default text", verbose_name="Text"
            ),
            preserve_default=False,
        ),
    ]