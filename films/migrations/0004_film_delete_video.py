# Generated by Django 4.2.5 on 2024-07-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
