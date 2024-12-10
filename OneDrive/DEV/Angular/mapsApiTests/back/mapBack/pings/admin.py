from django.contrib import admin
from .models import Ping
from .models import Tag


# Register your models here.
admin.site.register(Ping)
admin.site.register(Tag)