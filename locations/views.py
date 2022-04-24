from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ads.models import Location
from locations.serializers import LocationsSerializer


# class LocationViewSet(ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationsSerializer


class LocationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            serializer = LocationsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(serializer)
        except Location.DoesNotExist:
            return JsonResponse({"name": ["This field is required."]}, status=400)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            queryset = Location.objects.all()
            location = get_object_or_404(queryset, pk=pk)
            serializer = LocationsSerializer(location)
        except Location.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=400)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            queryset = Location.objects.all()
            location = get_object_or_404(queryset, pk=pk)

            serializer = LocationsSerializer(location, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(serializer)
        except Location.DoesNotExist:
            return JsonResponse({"name": ["This field is required."]}, status=400)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Location.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
