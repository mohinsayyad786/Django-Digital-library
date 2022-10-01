# Generated by Django 4.0.6 on 2022-07-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WORK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publication', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('is_deleted', models.CharField(max_length=10)),
            ],
        ),
    ]
