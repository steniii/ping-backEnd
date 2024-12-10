from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Ping, Tag
from .serializers import PingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as token_authentication
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User

class PingViewSet(viewsets.ModelViewSet):
    queryset = Ping.objects.all().order_by('-date')
    serializer_class = PingSerializer
    parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

    def create(self, request, *args, **kwargs):
        print("Données reçues :", request.data)  # Ajoutez cette ligne pour afficher les données envoyées
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("Données reçues :", request.data)
            serializer.save(creator_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Erreurs de validation :", serializer.errors)  # Affiche les erreurs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_path='search-by-tag')
    def search_by_tag(self, request):
        """
        Filtrer les Pings par un tag.
        """
        # Récupérer le tag à partir des paramètres de la requête
        # tag_name = request.query_params.get('tag', None)
        tag_name = request.query_params.get('tag', '').strip()
        if tag_name and not tag_name.startswith("#"):
            tag_name = f"#{tag_name}"
        print(request.query_params)
        if tag_name is not None:
            # Trouver le tag correspondant
            tag = Tag.objects.filter(name=tag_name).first()
            
            if tag:
                # Récupérer les pings associés à ce tag
                pings = Ping.objects.filter(tags=tag)
                # Sérialiser et renvoyer les pings
                serializer = PingSerializer(pings, many=True, context={'request': request})
                return Response(serializer.data)
            else:
                return Response({'message': 'Tag not found'}, status=404)
        return Response({'message': 'Tag parameter is required'}, status=400)
    
    @action(detail=False, methods=['get'], url_path='filter-by-profile')
    def filterById(self, request):
        """
        Filtrer les Pings par ID d'utilisateur.
        """
        profile_id = request.query_params.get('id', '').strip()
        if not profile_id:  # Vérifie si l'ID est fourni et non vide
            return Response({'message': 'Profile ID is required'}, status=400)

        try:
            # Trouver l'utilisateur correspondant à l'ID
            user = User.objects.get(id=profile_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)

        # Récupérer les Pings associés à cet utilisateur
        pings = Ping.objects.filter(creator_id=user)
        serializer = PingSerializer(pings, many=True, context={'request': request})
        return Response(serializer.data, status=200)