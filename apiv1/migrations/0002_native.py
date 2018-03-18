# Generated by Django 2.0.2 on 2018-03-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Native',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pic', models.FileField(blank=True, null=True, upload_to='pic/')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.IntegerField(blank=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
        ),
    ]