# Generated by Django 5.1.1 on 2024-09-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeform', '0016_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]