# Generated by Django 3.0.5 on 2020-07-18 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=30)),
                ('Contact', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Content', models.TextField()),
                ('Author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BLG.Author')),
            ],
        ),
    ]
