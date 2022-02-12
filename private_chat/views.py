# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .models import Detail
from .serializers import DetailModelSerializer

class GetAllData(APIView):
    def get(self, request):
        query = Detail.objects.all().order_by('-date')
        serializers = DetailModelSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

class PostModelData(APIView):
    def post(self, request):
        serializer = DetailModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditData(APIView):
    def get(self, request, pk):
        query = Detail.objects.get(pk=pk)
        serializer = DetailModelSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Detail.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        query = Detail.objects.get(pk=pk)
        serializer = DetailModelSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Detail.objects.filter(store_name__contains= search)
        serializer = DetailModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#
#
# def index(request):
#     return render(request, 'private_chat/index.html')
#
# def room(request, room_name):
#     return render(request, 'private_chat/room.html', {
#         'room_name': room_name
#     })