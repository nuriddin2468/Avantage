from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import TagListSerializer, EquipmentByTagSerializer, FullPageSerializer
from main.models import TagModel, FullPageModel
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse


class TagsListView(APIView):
    def get(self, request):
        tags = TagModel.objects.all()
        serializer = TagListSerializer(tags, many=True, context={"request": request})
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


class FullPageView(APIView):

    def get(self, request):
        page = get_object_or_404(FullPageModel, id=1)
        serializer = FullPageSerializer(page, context={"request": request})
        return Response(serializer.data)

class TelegramView(View):

    def post(self, request):
        return JsonResponse({'error': 0})