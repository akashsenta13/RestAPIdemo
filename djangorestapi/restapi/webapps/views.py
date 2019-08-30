from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Tech
from .serializer import TechSerializer

class AllTech(ListAPIView):

    queryset = Tech.objects.all()
    serializer_class = TechSerializer

    def post(self, request, format=None):
        serializer = TechSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechView(APIView):

    def get(self, request, pk, format=None):
        try:
            tech = Tech.objects.get(pk=pk)
            serializer = TechSerializer(tech)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tech = Tech.objects.get(pk=pk)
        tech.delete()
        return Response(status=status.HTTP_200_OK)
