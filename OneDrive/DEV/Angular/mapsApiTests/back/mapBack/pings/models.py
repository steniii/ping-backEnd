from django.db import models
import re

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

def extract_tags(description):
    description = description or ''
    # Utilisation d'une expression régulière pour trouver toutes les occurrences de #tag
    return re.findall(r'#[\w-]+', description)

# Create your models here.
class Ping(models.Model):
    #id auto by djnago orm
    creator_id = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='pings',null=True) 
    lattitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='pings/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='pings', blank=True)

    def save(self, *args, **kwargs):
        # Sauvegarde initiale pour générer un ID
        super().save(*args, **kwargs)

        # Extraire les tags depuis la description
        extracted_tags = extract_tags(self.description)
        
        # Ajouter ou associer les tags
        tags_to_add = []
        for tag_text in extracted_tags:
            tag, created = Tag.objects.get_or_create(name=tag_text)
            tags_to_add.append(tag)
        
        # Mettre à jour la relation ManyToMany
        self.tags.set(tags_to_add)  # Utilise `set()` pour éviter les doublons


    # def save(self, *args, **kwargs):
    #     # Sauvegarde initiale pour générer un ID
    #     super().save(*args, **kwargs)
        
    #     # Extraire les tags depuis la description
    #     extracted_tags = set(part for part in self.description.split() if part.startswith("#"))
        
    #     # Ajouter ou associer les tags
    #     for tag_text in extracted_tags:
    #         tag, created = Tag.objects.get_or_create(name=tag_text)
    #         self.tags.add(tag)

    # def save(self, *args, **kwargs):
    #     # Extraire les tags de la description
    #     self.tags.clear()
    #     extracted_tags = extract_tags(self.description)
        
    #     # Ajouter les tags extraits à l'objet Ping
    #     for tag_name in extracted_tags:
    #         tag, created = Tag.objects.get_or_create(name=tag_name)  # Créer le tag si il n'existe pas déjà
    #         self.tags.add(tag)  # Ajouter le tag à la relation ManyToMany
    #         if tag :
    #             print(f"Tag {tag.name} créé avec succès.")

    #     super().save(*args, **kwargs)  # Enregistrer l'objet Ping

    def __str__(self):
        return f'Ping by {self.description} at {self.lattitude}, {self.longitude}'