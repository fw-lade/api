from django.shortcuts import render
from rest_framework.decorators import api_view
from todo.serializer import TodoSerializer
from .models import Todo
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def createtodo(request):
    record = TodoSerializer(data = request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['GET'])
def alltodo(request):
    record = Todo.objects.all()
    info = TodoSerializer(record, many = True)
    return Response(info.data)

@api_view(['DELETE'])
def deletetodo(request, id):
    record = Todo.objects.get(id = id)
    record.delete()
    return Response('Todo deleted Successfully')

@api_view(['GET'])
def tododetails(request, id):
    record = Todo.objects.get(id = id)
    info = TodoSerializer(record, many = False)
    return Response(info.data)

@api_view(['GET'])
def todoedit(request, id):
    record = Todo.objects.get(id = id)
    info = TodoSerializer(data = request.data, instance = record)
    if info.is_valid():
        info.save()
        return Response('Updated Successfully')