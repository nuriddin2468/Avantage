# Generated by Django 3.0.7 on 2020-07-13 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200708_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Остальные возможности',
                'verbose_name_plural': 'Остальные возможности',
            },
        ),
        migrations.AlterModelOptions(
            name='eventsmodel',
            options={'verbose_name': 'Ивент', 'verbose_name_plural': 'Ивенты'},
        ),
        migrations.AlterField(
            model_name='aboutusmodel',
            name='carousel',
            field=models.ManyToManyField(related_name='about_us', to='main.ImagesModel', verbose_name='Карусель изображений'),
        ),
        migrations.AlterField(
            model_name='aboutusmodel',
            name='image_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ImagesModel', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='aboutusmodel',
            name='video',
            field=models.FileField(upload_to='video/', verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='cateringmodel',
            name='carousel',
            field=models.ManyToManyField(related_name='catering', to='main.ImagesModel', verbose_name='Карусель изображений'),
        ),
        migrations.AlterField(
            model_name='cateringmodel',
            name='events',
            field=models.ManyToManyField(to='main.EventsModel', verbose_name='Ивенты'),
        ),
        migrations.AlterField(
            model_name='equipmentmodel',
            name='en_title',
            field=models.CharField(default='', max_length=120, verbose_name='Название(en)'),
        ),
        migrations.AlterField(
            model_name='equipmentmodel',
            name='img',
            field=models.ImageField(default='', upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='equipmentmodel',
            name='price',
            field=models.IntegerField(default=199, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='equipmentmodel',
            name='ru_title',
            field=models.CharField(default='', max_length=120, verbose_name='Название(ru)'),
        ),
        migrations.AlterField(
            model_name='equipmentmodel',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='main.TagModel', verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='eventsmodel',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='imagesmodel',
            name='alt',
            field=models.CharField(default='', max_length=120, verbose_name='название фотографии'),
        ),
        migrations.AlterField(
            model_name='imagesmodel',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='carousel',
            field=models.ManyToManyField(related_name='register', to='main.ImagesModel', verbose_name='Карусель изображений'),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='events',
            field=models.ManyToManyField(related_name='register', to='main.EventsModel', verbose_name='Ивенты'),
        ),
        migrations.AlterField(
            model_name='standmodel',
            name='carousel',
            field=models.ManyToManyField(related_name='stand', to='main.ImagesModel', verbose_name='Карусель изображений'),
        ),
        migrations.AlterField(
            model_name='standmodel',
            name='video',
            field=models.FileField(upload_to='video/', verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='en_title',
            field=models.CharField(default='', max_length=120, verbose_name='Название(en)'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='ru_title',
            field=models.CharField(default='', max_length=120, verbose_name='Название(ru)'),
        ),
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('carousel', models.ManyToManyField(related_name='portfolio', to='main.ImagesModel')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
        migrations.AddField(
            model_name='registermodel',
            name='other',
            field=models.ManyToManyField(to='main.OtherModel', verbose_name='Дополнительные возможности'),
        ),
    ]