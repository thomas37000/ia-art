# Generated by Django 4.2.3 on 2023-07-14 15:45

from django.db import migrations, models
import ia_art.models


class Migration(migrations.Migration):

    dependencies = [
        ('ia_art', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ia_art/paintings/', validators=[ia_art.models.validate_image_size])),
                ('image_url', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='paintings',
            field=models.ManyToManyField(blank=True, to='ia_art.painting'),
        ),
    ]
