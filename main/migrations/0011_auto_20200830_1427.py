# Generated by Django 3.0.7 on 2020-08-30 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200830_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullpagemodel',
            name='aboutSection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aboutSection', to='main.AboutUsModel'),
        ),
        migrations.AlterField(
            model_name='fullpagemodel',
            name='cateringSection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cateringSection', to='main.CateringModel'),
        ),
        migrations.AlterField(
            model_name='fullpagemodel',
            name='registerSection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registerSection', to='main.RegisterModel'),
        ),
        migrations.AlterField(
            model_name='fullpagemodel',
            name='standSection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standSection', to='main.StandModel'),
        ),
    ]