from rest_framework import serializers
from main.models import *


class TagListRUSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='ru_title')

    class Meta:
        model = TagModel
        fields = ("id", "title", )

class TagListENSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='en_title')

    class Meta:
        model = TagModel
        fields = ("id", "title",)


class EquipmentDetailRUSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField('get_img_url')
    title = serializers.CharField(source='ru_title')
    tag = TagListRUSerializer()

    class Meta:
        model = EquipmentModel
        fields = ("id", "title", "img", "price", "tag")

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.img.url)


class EquipmentDetailENSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField('get_img_url')
    title = serializers.CharField(source='en_title')
    tag = TagListENSerializer()

    class Meta:
        model = EquipmentModel
        fields = ("id", "title", "img", "price", "tag")

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.img.url)



class EquipmentByTagRUSerializer(serializers.ModelSerializer):
    equipments = EquipmentDetailRUSerializer(many=True)

    class Meta:
        model = TagModel
        exclude = ("ru_title", "en_title")
        depth = 1


class EquipmentByTagENSerializer(serializers.ModelSerializer):
    equipments = EquipmentDetailENSerializer(many=True)

    class Meta:
        model = TagModel
        exclude = ("ru_title", "en_title")
        depth = 1


class PortfolioListRUSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='ru_title')

    class Meta:
        model = PortfolioModel
        fields = ("id", "title", "image")


class PortfolioListENSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='ru_title')

    class Meta:
        model = PortfolioModel
        fields = ("id", "title", "image")


class ImagesRUSerializer(serializers.ModelSerializer):
    alt = serializers.CharField(source='ru_alt')

    class Meta:
        model = ImagesModel
        fields = ("id", "alt", "image")


class ImagesENSerializer(serializers.ModelSerializer):
    alt = serializers.CharField(source='en_alt')

    class Meta:
        model = ImagesModel
        fields = ("id", "alt", "image")


class PortfolioRUSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='ru_title')
    text = serializers.CharField(source='ru_text')
    carousel = ImagesRUSerializer(many=True)

    class Meta:
        model = PortfolioModel
        fields = ("id", "title", "text", "carousel")
        depth = 2


class PortfolioENSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='en_title')
    text = serializers.CharField(source='en_text')
    carousel = ImagesENSerializer(many=True)

    class Meta:
        model = PortfolioModel
        fields = ("id", "title", "text", "carousel")
        depth = 2


#fullpage
class AboutSectionRUSerializer(serializers.ModelSerializer):
    image_1 = ImagesRUSerializer()
    carousel = ImagesRUSerializer(many=True)

    class Meta:
        model = AboutUsModel
        fields = ("image_1", "video", "carousel")


class AboutSectionENSerializer(serializers.ModelSerializer):
    image_1 = ImagesENSerializer()
    carousel = ImagesENSerializer(many=True)

    class Meta:
        model = AboutUsModel
        fields = ("image_1", "video", "carousel")


class EventsRUSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='ru_title')

    class Meta:
        model = EventsModel
        fields = ("title", )


class EventsENSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='en_title')

    class Meta:
        model = EventsModel
        fields = ("title", )


class CateringSectionRUSerializer(serializers.ModelSerializer):
    carousel = ImagesRUSerializer(many=True)
    events = EventsRUSerializer(many=True)

    class Meta:
        model = CateringModel
        fields = ("carousel", "events")


class CateringSectionENSerializer(serializers.ModelSerializer):
    carousel = ImagesENSerializer(many=True)
    events = EventsENSerializer(many=True)

    class Meta:
        model = CateringModel
        fields = ("carousel", "events")


class StandSectionRUSerializer(serializers.ModelSerializer):
    carousel = ImagesRUSerializer(many=True)

    class Meta:
        model = StandModel
        fields = ("carousel", "video")


class StandSectionENSerializer(serializers.ModelSerializer):
    carousel = ImagesENSerializer(many=True)

    class Meta:
        model = StandModel
        fields = ("carousel", "video")


class OtherRUSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='ru_title')

    class Meta:
        model = OtherModel
        fields = ("id", "title", )


class OtherENSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='en_title')

    class Meta:
        model = OtherModel
        fields = ("id", "title", )


class RegisterSectionRUSerializer(serializers.ModelSerializer):
    events = EventsRUSerializer(many=True)
    carousel = ImagesRUSerializer(many=True)
    other = OtherRUSerializer(many=True)

    class Meta:
        model = RegisterModel
        fields = ("events", "carousel", "other")


class RegisterSectionENSerializer(serializers.ModelSerializer):
    events = EventsENSerializer(many=True)
    carousel = ImagesENSerializer(many=True)
    other = OtherENSerializer(many=True)

    class Meta:
        model = RegisterModel
        fields = ("events", "carousel", "other")


class FullPageRUSerializer(serializers.ModelSerializer):
    aboutSection = AboutSectionRUSerializer()
    cateringSection = CateringSectionRUSerializer()
    standSection = StandSectionRUSerializer()
    registerSection = RegisterSectionRUSerializer()

    class Meta:
        model = FullPageModel
        fields = ("id", "aboutSection", "cateringSection", "standSection", "registerSection")
        depth = 2


class FullPageENSerializer(serializers.ModelSerializer):
    aboutSection = AboutSectionENSerializer()
    cateringSection = CateringSectionENSerializer()
    standSection = StandSectionENSerializer()
    registerSection = RegisterSectionENSerializer()

    class Meta:
        model = FullPageModel
        fields = ("id", "aboutSection", "cateringSection", "standSection", "registerSection")
        depth = 2
