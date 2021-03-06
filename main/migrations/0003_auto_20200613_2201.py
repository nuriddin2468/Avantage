# Generated by Django 3.0.7 on 2020-06-13 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_equipmentmodel_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentmodel',
            old_name='title',
            new_name='ru_title',
        ),
        migrations.RenameField(
            model_name='tagmodel',
            old_name='title',
            new_name='ru_title',
        ),
        migrations.AddField(
            model_name='equipmentmodel',
            name='en_title',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='tagmodel',
            name='en_title',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='equipmentmodel',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='main.TagModel'),
        ),
    ]
