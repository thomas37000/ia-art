from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Artist
from .serializers import ArtistSerializer


@api_view(["GET", "POST"])
def ia_art(request):
    if request.method == "GET":
        data = Artist.objects.all()
        serializer = ArtistSerializer(data, many=True)
        return Response({"artists": serializer.data})

    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"artist": serializer.data}, status=status.HTTP_201_CREATED)
        # if POST request false
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get artist detail by id
@api_view(["GET", "POST", "PUT", "DELETE"])
def artist(request, id):
    try:
        data = Artist.objects.get(pk=id)  # pk = primary key
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArtistSerializer(data)
        return Response({"artist": serializer.data})

    elif request.method == "POST":
        serializer = ArtistSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"artist": serializer.data})
        # if POST request false
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        serializer = ArtistSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"artist": serializer.data})
        # if PUT request false
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
