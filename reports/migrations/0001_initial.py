# Generated by Django 5.0.6 on 2024-07-11 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0003_remove_attachment_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('SPAM', 'Spam, scam or fraudulent post'), ('HATE', 'Hate speech and/or abusive content'), ('ILLEGAL', 'Illegal content'), ('OTHER', 'Other')], max_length=100)),
                ('reason', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reported_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_post', to='posts.post')),
                ('reporting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_user_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('SPAM', 'Spamming, scamming or fraudulent behaviour'), ('HATE', 'Hate speech and/or abusive behaviour'), ('ILLEGAL', 'Illegal activities'), ('OTHER', 'Other')], max_length=100)),
                ('reason', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reported_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_user', to=settings.AUTH_USER_MODEL)),
                ('reporting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_user_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
