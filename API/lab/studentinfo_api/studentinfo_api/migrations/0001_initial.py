# Generated by Django 3.2.16 on 2022-11-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('Course', models.CharField(max_length=100)),
                ('College', models.CharField(max_length=500)),
            ],
        ),
    ]
