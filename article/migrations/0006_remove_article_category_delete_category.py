# Generated by Django 5.0.1 on 2024-01-26 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
