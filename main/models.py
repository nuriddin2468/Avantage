from django.db import models


class TagModel(models.Model):
    ru_title = models.CharField(max_length=120, default="")
    en_title = models.CharField(max_length=120, default="")

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class EquipmentModel(models.Model):
    ru_title = models.CharField(max_length=120, default="")
    en_title = models.CharField(max_length=120, default="")
    img = models.ImageField(default="")
    price = models.IntegerField(default=199)
    tag = models.ForeignKey(TagModel, related_name="equipments", on_delete=models.CASCADE)

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'


class ImagesModel(models.Model):
    alt = models.CharField(max_length=120, default="")
    image = models.ImageField(default="")

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class AboutUsModel(models.Model):
    image_1 = models.ForeignKey(ImagesModel, on_delete=models.CASCADE)
    carousel = models.ManyToManyField(ImagesModel, related_name='about_us')
    video = models.FileField(upload_to='video/')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class EventsModel(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ивенты'
        verbose_name_plural = 'Ивенты'


class CateringModel(models.Model):
    carousel = models.ManyToManyField(ImagesModel, related_name='catering')
    events = models.ManyToManyField(EventsModel)

    class Meta:
        verbose_name = 'Кейтеринг'
        verbose_name_plural = 'Кейтеринг'


class StandModel(models.Model):
    carousel = models.ManyToManyField(ImagesModel, related_name='stand')
    video = models.FileField(upload_to='video/')

    class Meta:
        verbose_name = 'Стэнды'
        verbose_name_plural = 'Стэнды'


class RegisterModel(models.Model):
    events = models.ManyToManyField(EventsModel, related_name='register')
    carousel = models.ManyToManyField(ImagesModel, related_name='register')

    class Meta:
        verbose_name = 'Регистрация посетителей'
        verbose_name_plural = 'Регистрация посетителей'


class FullPageModel(models.Model):
    aboutSection = models.ForeignKey(AboutUsModel, on_delete=models.CASCADE)
    cateringSection = models.ForeignKey(CateringModel, on_delete=models.CASCADE)
    standSection = models.ForeignKey(StandModel, on_delete=models.CASCADE)
    registerSection = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)