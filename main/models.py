from django.db import models


class TagModel(models.Model):
    ru_title = models.CharField(max_length=120, default="", verbose_name='Название(ru)')
    en_title = models.CharField(max_length=120, default="", verbose_name='Название(en)')

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class EquipmentModel(models.Model):
    ru_title = models.CharField(max_length=120, default="", verbose_name='Название(ru)')
    en_title = models.CharField(max_length=120, default="", verbose_name='Название(en)')
    img = models.ImageField(default="", verbose_name='Изображение')
    price = models.IntegerField(default=199, verbose_name='Цена')
    tag = models.ForeignKey(TagModel, related_name="equipments", verbose_name='Тэг', on_delete=models.CASCADE)

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'


class ImagesModel(models.Model):
    ru_alt = models.CharField(max_length=120, default="", verbose_name='название фотографии(ru)')
    en_alt = models.CharField(max_length=120, default="", verbose_name='название фотографии(en)')
    image = models.ImageField(default="", verbose_name='Изображение')

    def __str__(self):
        return self.ru_alt

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class AboutUsModel(models.Model):
    image_1 = models.ForeignKey(ImagesModel, on_delete=models.CASCADE, verbose_name='Изображение')
    carousel = models.ManyToManyField(ImagesModel, related_name='about_us', verbose_name='Карусель изображений')
    video = models.FileField(upload_to='video/', verbose_name='Видео')

    class Meta:
        verbose_name = '4. О нас'
        verbose_name_plural = '4. О нас'


class EventsModel(models.Model):
    ru_title = models.CharField(max_length=120, default="", verbose_name='Название(ru)')
    en_title = models.CharField(max_length=120, default="", verbose_name='Название(en)')

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = 'Ивент'
        verbose_name_plural = 'Ивенты'


class CateringModel(models.Model):
    carousel = models.ManyToManyField(ImagesModel, related_name='catering', verbose_name='Карусель изображений')
    events = models.ManyToManyField(EventsModel, verbose_name='Ивенты')

    class Meta:
        verbose_name = '2. Кейтеринг'
        verbose_name_plural = '2. Кейтеринг'


class StandModel(models.Model):
    carousel = models.ManyToManyField(ImagesModel, related_name='stand', verbose_name='Карусель изображений')
    video = models.FileField(upload_to='video/', verbose_name='Видео')

    class Meta:
        verbose_name = '1. Стэнды'
        verbose_name_plural = '1. Стэнды'


class OtherModel(models.Model):
    ru_title = models.CharField(max_length=120, default="", verbose_name="Название(ru)")
    en_title = models.CharField(max_length=120, default="", verbose_name="Название(en)")

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = "Остальные возможности"
        verbose_name_plural = "Остальные возможности"


class RegisterModel(models.Model):
    events = models.ManyToManyField(EventsModel, related_name='register', verbose_name='Ивенты')
    other = models.ManyToManyField(OtherModel, verbose_name="Дополнительные возможности")
    carousel = models.ManyToManyField(ImagesModel, related_name='register', verbose_name='Карусель изображений')

    class Meta:
        verbose_name = '3. Регистрация посетителей'
        verbose_name_plural = '3. Регистрация посетителей'


class FullPageModel(models.Model):
    aboutSection = models.ForeignKey(AboutUsModel, related_name="aboutSection", on_delete=models.CASCADE)
    cateringSection = models.ForeignKey(CateringModel, related_name="cateringSection", on_delete=models.CASCADE)
    standSection = models.ForeignKey(StandModel, related_name="standSection", on_delete=models.CASCADE)
    registerSection = models.ForeignKey(RegisterModel, related_name="registerSection", on_delete=models.CASCADE)


class PortfolioModel(models.Model):
    ru_title = models.CharField(max_length=120, default="", verbose_name="название(ru)")
    en_title = models.CharField(max_length=120, default="", verbose_name="название(en)")
    image = models.ImageField()
    en_text = models.TextField(default="", verbose_name="текст(en)")
    ru_text = models.TextField(default="", verbose_name="текст(ru)")
    carousel = models.ManyToManyField(ImagesModel, related_name='portfolio')

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"