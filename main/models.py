from django.db import models


class TagModel(models.Model):
    ru_title = models.CharField(max_length=120, default="")
    en_title = models.CharField(max_length=120, default="")

    def __str__(self):
        return self.ru_title


class EquipmentModel(models.Model):
    ru_title = models.CharField(max_length=120, default="")
    en_title = models.CharField(max_length=120, default="")
    img = models.ImageField(default="")
    price = models.IntegerField(default=199)
    tag = models.ForeignKey(TagModel, related_name="equipments", on_delete=models.CASCADE)

    def __str__(self):
        return self.ru_title
