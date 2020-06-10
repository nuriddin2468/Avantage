from rest_framework import serializers
from main.models import TagModel, EquipmentModel


class TagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagModel
        fields = ("id", "title")


class EquipmentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentModel
        fields = "__all__"


class EquipmentByTagSerializer(serializers.ModelSerializer):
    equipments = EquipmentDetailSerializer(many=True)

    class Meta:
        model = TagModel
        fields = ("id", "title", "equipments")