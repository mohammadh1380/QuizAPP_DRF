# Generated by Django 4.0.3 on 2022-03-05 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_question_answer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Options',
        ),
    ]
