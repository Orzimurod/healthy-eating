# Generated by Django 5.0.4 on 2024-12-09 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_blog_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
    ]
