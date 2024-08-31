# Generated by Django 4.2.4 on 2023-08-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snake',
            name='name',
        ),
        migrations.AddField(
            model_name='snake',
            name='submission_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='snake',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
