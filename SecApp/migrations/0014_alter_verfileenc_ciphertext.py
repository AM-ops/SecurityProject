# Generated by Django 3.2.3 on 2021-05-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecApp', '0013_auto_20210530_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verfileenc',
            name='ciphertext',
            field=models.FileField(default='file.png', upload_to='media/'),
        ),
    ]