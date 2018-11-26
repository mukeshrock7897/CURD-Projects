from rest_framework import serializers
from .models import Album,Track


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model=Track

        fields="__all__"
        depth=1
  #      depth=2

class AlbumSerializer(serializers.Serializer):
    tracks = TrackSerializer(many=True)


    class Meta:
        model=Album
        fields = ('album_name', 'artist', 'tracks')

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

