# Generated by Django 2.0.2 on 2018-03-14 12:54

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='body',
            field=markdownx.models.MarkdownxField(null=True),
        ),
    ]
