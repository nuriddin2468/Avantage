from django.db import models


class TagModel(models.Model):
    title = models.CharField(max_length=120, default="")


class EquipmentModel(models.Model):
    title = models.CharField(max_length=120, default="")
    img = models.ImageField(default="")
    tag = models.ForeignKey(TagModel, related_name="equipments", on_delete=models.CASCADE)