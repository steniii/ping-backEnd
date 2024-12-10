from rest_framework import serializers
from .models import Ping, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PingSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    image = serializers.ImageField(required=False)  # Permettre l'upload d'images

    class Meta:
        model = Ping
        fields =  ['id','creator_id','lattitude', 'longitude', 'description', 'image', 'date', 'tags']
        read_only_fields = ['id', 'creator_id', 'date']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])  # Extraire les tags de la requête
        creator_id = validated_data.pop('creator_id')  # Associer l'utilisateur
        ping = Ping.objects.create(creator_id=creator_id, **validated_data)
        
        # Gérer les tags associés
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            ping.tags.add(tag)

        return ping

    def to_representation(self, instance):
        # Convertit l'objet en représentation pour l'API
        representation = super().to_representation(instance)
        if instance.image:
            # Générer une URL absolue pour l'image
            request = self.context.get('request')
            representation['image'] = request.build_absolute_uri(instance.image.url)
        return representation
