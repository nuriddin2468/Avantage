# Generated by Django 3.0.7 on 2020-07-08 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200615_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(default='', max_length=120)),
                ('image', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/')),
                ('carousel', models.ManyToManyField(related_name='stand', to='main.ImagesModel')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ManyToManyField(related_name='register', to='main.ImagesModel')),
                ('events', models.ManyToManyField(related_name='register', to='main.EventsModel')),
            ],
        ),
        migrations.CreateModel(
            name='CateringModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ManyToManyField(related_name='catering', to='main.ImagesModel')),
                ('events', models.ManyToManyField(to='main.EventsModel')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/')),
                ('carousel', models.ManyToManyField(related_name='about_us', to='main.ImagesModel')),
                ('image_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ImagesModel')),
            ],
        ),
    ]
