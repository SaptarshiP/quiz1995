# Generated by Django 2.1.15 on 2020-06-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_bank',
            name='option4',
            field=models.CharField(max_length=100, null=True),
        ),
    ]