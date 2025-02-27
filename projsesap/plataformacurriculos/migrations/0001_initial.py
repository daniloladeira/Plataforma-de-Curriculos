# Generated by Django 5.1.5 on 2025-01-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='E-Mail')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('desired_position', models.CharField(max_length=100, verbose_name='Desired Position')),
                ('escolarity', models.CharField(choices=[('high_school', 'High School'), ('bachelors', 'Bachelors'), ('masters', 'Masters'), ('phd', 'PhD')], max_length=100, verbose_name='Escolarity')),
                ('observations', models.CharField(max_length=100, verbose_name='Observations')),
                ('curriculum_archive', models.FileField(upload_to='projsesap\\plataformacurriculos\\curriculums', verbose_name='Upload the Curriculum')),
            ],
        ),
    ]
