# Generated by Django 3.2.3 on 2021-05-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecApp', '0021_auto_20210531_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vigfileenc',
            name='ciphertext',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='vigfileenc',
            name='plaintext',
            field=models.FileField(upload_to=''),
        ),
    ]