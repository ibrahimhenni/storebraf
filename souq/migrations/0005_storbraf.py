# Generated by Django 4.0 on 2022-03-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souq', '0004_product_aff_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storbraf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('about_us', models.TextField(max_length=1000)),
                ('privacy_policy', models.TextField(max_length=1000)),
            ],
        ),
    ]
