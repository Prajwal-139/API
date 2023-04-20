from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BookMyShowSer
from .models import BookMyShow

class GetPost(APIView):
    def get(self,r):
        Bookobj = BookMyShow.objects.all()
        serobj = BookMyShowSer(Bookobj,many=True)
        return Response(serobj.data)

    def post(self,r):
        serobj = BookMyShowSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateDelete(APIView):
    def put(self,r,pk):
        bookingDetails = BookMyShow.objects.get(pk=pk)
        serobj = BookMyShowSer(bookingDetails,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        serobj = BookMyShow.objects.get(pk=pk)
        serobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)