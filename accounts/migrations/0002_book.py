# Generated by Django 3.1.5 on 2021-02-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=40)),
                ('isbn', models.PositiveIntegerField()),
                ('no_of_copies', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
