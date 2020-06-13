from rest_framework import serializers
from main.models import TagModel, EquipmentModel


class TagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagModel
        fields = "__all__"


class EquipmentDetailSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField('get_img_url')

    class Meta:
        model = EquipmentModel
        fields = "__all__"

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.img.url)


class EquipmentByTagSerializer(serializers.ModelSerializer):
    equipments = EquipmentDetailSerializer(many=True)

    class Meta:
        model = TagModel
        fields = ("id", "ru_title", "en_title", "equipments")