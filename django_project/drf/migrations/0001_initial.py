# Generated by Django 3.0.7 on 2020-06-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_link', models.CharField(max_length=7, verbose_name='Short link')),
                ('full_link', models.CharField(max_length=500, verbose_name='Full link')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
    ]
