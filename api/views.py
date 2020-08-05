from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task,My
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'my_list':'/task-list-my/',
        'Deati view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



class my(APIView):
    def get(self,request):
        task = My.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def task_detail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def task_update(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['DELETE'])
def task_delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()