# Generated by Django 4.0.3 on 2022-04-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='C:\\Users\\HP\\OneDrive\\Desktop\\ZEN\\zen\\zen\\static\\assets\\images\\Logo.png')),
            ],
        ),
    ]
