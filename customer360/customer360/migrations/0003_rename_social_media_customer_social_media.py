# Generated by Django 5.1.7 on 2025-03-19 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0002_customer_social_media_alter_interaction_channel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Social_media',
            new_name='social_media',
        ),
    ]
