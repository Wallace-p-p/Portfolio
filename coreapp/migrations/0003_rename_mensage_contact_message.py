# Generated by Django 4.0.1 on 2022-08-27 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mensage',
            new_name='message',
        ),
    ]
