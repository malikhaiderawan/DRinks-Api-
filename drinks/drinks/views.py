from operator import imod
from urllib import response

from .serializer import malikserializer
from .models import malik
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def malik_list(request):
    if request.method == 'GET':
        foz=malik.objects.all()
        serializer=malikserializer(foz,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=malikserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def malik_details(request,id):
    try:
        fiza=malik.objects.get(pk=id)
    except malik.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method=='GET':
        serializer=malikserializer(fiza)
        return Response(serializer.data)

    if request.method=='PUT':
        serializer=malikserializer(fiza,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method=='DELETE':
        fiza.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
