from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from graph import models, serializers


@api_view(['GET'])
def get_graphs(request):
    return Response("zwrotka restowa")


class GraphList(generics.ListAPIView):
    serializer_class = serializers.GraphSerializer
    def get_queryset(self):
        return models.Graph.objects.all()


class GraphDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Graph.objects.all()
    serializer_class = serializers.GraphSerializer


class GraphCreate(generics.CreateAPIView):
    serializer_class = serializers.GraphSerializer
    def get_queryset(self):
        return models.Graph.objects.all()

    def perform_create(self, serializer):
        """ 
        dopisać tworzenie macierzy
        """
        pass

