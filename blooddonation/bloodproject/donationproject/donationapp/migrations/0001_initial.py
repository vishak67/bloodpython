# Generated by Django 3.2.9 on 2022-02-05 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='center')),
            ],
            options={
                'verbose_name': 'center',
                'verbose_name_plural': 'centers',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='district')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donationapp.centers')),
            ],
            options={
                'verbose_name': 'district',
                'verbose_name_plural': 'districts',
                'ordering': ('name',),
            },
        ),
    ]