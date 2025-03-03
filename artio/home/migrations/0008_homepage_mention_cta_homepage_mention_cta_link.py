# Generated by Django 5.0.10 on 2025-01-16 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_homepage_mention_cta_and_more'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='mention_cta',
            field=models.CharField(blank=True, help_text='Contact forms CTA', max_length=255, verbose_name='Contact CTA'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='mention_cta_link',
            field=models.ForeignKey(blank=True, help_text='contact Page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Contact CTA link'),
        ),
    ]
