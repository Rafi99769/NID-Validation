# Generated by Django 2.1.7 on 2019-03-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fathers_name', models.CharField(max_length=50)),
                ('mothers_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('blood_group', models.PositiveSmallIntegerField(choices=[(1, 'A+'), (2, 'B+'), (3, 'O+'), (4, 'AB+'), (5, 'A-'), (6, 'B-'), (7, 'O-'), (8, 'AB-')], default=3)),
                ('received_date', models.DateField()),
            ],
        ),
    ]
