# Generated by Django 5.0.6 on 2024-07-10 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_attachment_owner_alter_attachment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='owner',
        ),
    ]
