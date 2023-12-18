# Generated by Django 4.2.7 on 2023-12-17 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_rename_waterquality_waterpotability'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TV_Ad_Budget', models.FloatField()),
                ('Radio_Ad_Budget', models.FloatField()),
                ('Newspaper_Ad_Budget', models.FloatField()),
                ('Sales', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
