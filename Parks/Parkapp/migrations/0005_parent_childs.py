# Generated by Django 3.0.5 on 2020-05-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parkapp', '0004_parkimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent_Childs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parent_Username', models.CharField(max_length=50)),
                ('Child_Username', models.CharField(max_length=50)),
            ],
        ),
    ]
