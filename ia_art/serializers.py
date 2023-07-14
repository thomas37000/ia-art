from rest_framework import serializers
from .models import Artist
from .models import Movement
from .models import Painting

class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = "__all__"


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    movements = MovementSerializer(many=True)
    paintings = PaintingSerializer(many=True)

    class Meta:
        model = Artist
        fields = "__all__"
