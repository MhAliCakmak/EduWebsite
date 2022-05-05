# Generated by Django 4.0.3 on 2022-04-28 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionApp', '0022_rename_slug_categories_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test', to='questionApp.test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.ImageField(upload_to='static/Test'),
        ),
    ]