# Generated by Django 5.0.10 on 2025-01-19 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standardpages', '0003_policypage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policypage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='MentionPage',
        ),
        migrations.DeleteModel(
            name='PolicyPage',
        ),
    ]
