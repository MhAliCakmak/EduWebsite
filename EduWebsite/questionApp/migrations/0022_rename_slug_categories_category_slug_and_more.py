# Generated by Django 4.0.3 on 2022-04-27 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionApp', '0021_test_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='slug',
            new_name='category_slug',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='slug',
            new_name='question_slug',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='slug',
            new_name='test_slug',
        ),
    ]