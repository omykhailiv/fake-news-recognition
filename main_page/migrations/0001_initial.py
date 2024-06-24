# Generated by Django 5.0.4 on 2024-05-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckedTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, unique=True)),
                ('prediction', models.CharField(max_length=8)),
                ('score', models.IntegerField(max_length=32)),
            ],
        ),
    ]