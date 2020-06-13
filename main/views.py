from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import TagListSerializer, EquipmentByTagSerializer
from main.models import TagModel
from django.shortcuts import get_object_or_404


class TagsListView(APIView):
    def get(self, request):
        tags = TagModel.objects.all()
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        tag = TagListSerializer(data=request.data)
        if tag.is_valid():
            tag.save()
        return Response(status=201)


class TagView(APIView):

    def get(self, request, pk):
        tag = get_object_or_404(TagModel, id=pk)
        serializer = EquipmentByTagSerializer(tag, context={"request": request})
        return Response(serializer.data)