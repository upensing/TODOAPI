from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from api.models import Task
from api.ser import TaskSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


def Entry(request):
    allToDo = Task.objects.all()
    print(allToDo)
    return HttpResponse("All ToDo Comming Soon...")


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    print(request.data)
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def taskDelete(request, taskId):
    task = Task.objects.get(id = taskId)
    task.delete()
    return Response("Task successfully deleted")

