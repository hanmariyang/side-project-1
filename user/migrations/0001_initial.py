# Generated by Django 4.2 on 2023-04-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=255)),
                ('birth_day', models.IntegerField(max_length=255)),
            ],
            options={
                'db_table': 'it_user',
            },
        ),
    ]