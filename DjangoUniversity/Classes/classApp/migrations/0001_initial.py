# Generated by Django 4.0.5 on 2022-06-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=64)),
                ('courseNumber', models.IntegerField(default='', max_length=16)),
                ('instructorName', models.CharField(default='', max_length=32)),
                ('duration', models.FloatField(default='', max_length=64)),
            ],
        ),
    ]