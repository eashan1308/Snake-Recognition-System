# Generated by Django 4.2.7 on 2023-11-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake_app', '0009_alter_deeplearningmodel_architecture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deeplearningmodel',
            name='weights',
            field=models.FileField(upload_to='models/'),
        ),
    ]
