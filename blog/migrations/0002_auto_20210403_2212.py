# Generated by Django 3.1.7 on 2021-04-03 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category_id',
            new_name='category',
        ),
    ]
