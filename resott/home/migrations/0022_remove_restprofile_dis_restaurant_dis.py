# Generated by Django 4.0.1 on 2022-06-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_restaurant_dis_restprofile_dis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restprofile',
            name='dis',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='dis',
            field=models.IntegerField(default=0),
        ),
    ]