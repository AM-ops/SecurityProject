# Generated by Django 3.2.3 on 2021-05-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecApp', '0014_alter_verfileenc_ciphertext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verfileenc',
            name='ciphertext',
            field=models.FileField(default='file.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='verfileenc',
            name='plaintext',
            field=models.FileField(upload_to=''),
        ),
    ]