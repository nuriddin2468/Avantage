from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import *
from main.models import TagModel, FullPageModel, PortfolioModel
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import telegram_test


class TagsListView(APIView):
    def get(self, request):
        tags = TagModel.objects.all()
        if "en" == self.request.headers['Content-Language']:
            serializer = TagListENSerializer(tags, many=True, context={"request": request})
            return Response(serializer.data)
        else:
            serializer = TagListRUSerializer(tags, many=True, context={"request": request})
            return Response(serializer.data)

    def post(self, request):
        tag = TagListRUSerializer(data=request.data)
        if tag.is_valid():
            tag.save()
        return Response(status=201)


class TagView(APIView):
    def get(self, request, pk):
        tag = get_object_or_404(TagModel, id=pk)
        if "en" == self.request.headers['Content-Language']:
            serializer = EquipmentByTagENSerializer(tag, context={"request": request})
            return Response(serializer.data)
        else:
            serializer = EquipmentByTagRUSerializer(tag, context={"request": request})
            return Response(serializer.data)


class FullPageView(APIView):
    def get(self, request):
        page = get_object_or_404(FullPageModel, id=1)
        if "en" == self.request.headers['Content-Language']:
            serializer = FullPageENSerializer(page, context={"request": request})
            return Response(serializer.data)
        else:
            serializer = FullPageRUSerializer(page, context={"request": request})
            return Response(serializer.data)


class PortfolioListView(APIView):
    def get(self, request):
        items = PortfolioModel.objects.all()
        if "en" == self.request.headers['Content-Language']:
            serializer = PortfolioListENSerializer(items, many=True ,context={"request": request})
            return Response(serializer.data)
        else:
            serializer = PortfolioListRUSerializer(items, many=True, context={"request": request})
            return Response(serializer.data)


class PortfolioView(APIView):
    def get(self, request, pk):
        tag = get_object_or_404(PortfolioModel, id=pk)
        if "en" == self.request.headers['Content-Language']:
            serializer = PortfolioENSerializer(tag, context={"request": request})
            return Response(serializer.data)
        else:
            serializer = PortfolioRUSerializer(tag, context={"request": request})
            return Response(serializer.data)


class TelegramView(APIView):
    @csrf_exempt
    def post(self, request):
        telegram_test(request.data)
        return JsonResponse({'error': 0})