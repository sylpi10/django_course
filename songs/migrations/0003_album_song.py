# Generated by Django 3.0.7 on 2020-06-09 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('songs', '0002_delete_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No name', max_length=255)),
                ('duration', models.IntegerField(default=0, help_text='duration in seconds')),
                ('lyrics', models.TextField(blank=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Album')),
            ],
        ),
    ]