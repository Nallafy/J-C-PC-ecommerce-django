# Generated by Django 3.2.3 on 2021-10-19 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211019_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='category_images'),
        ),
    ]