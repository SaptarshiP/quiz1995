# Generated by Django 2.1.15 on 2020-06-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_roll_number', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=20)),
                ('student_class', models.CharField(max_length=5)),
                ('student_section', models.CharField(max_length=5)),
                ('student_mother_name', models.CharField(max_length=20)),
                ('student_father_name', models.CharField(max_length=20)),
                ('student_address', models.CharField(max_length=50)),
            ],
        ),
    ]
