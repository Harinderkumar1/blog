# Generated by Django 4.1.3 on 2022-12-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('suggestion', models.TextField()),
            ],
        ),
    ]