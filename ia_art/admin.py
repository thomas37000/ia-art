from django.contrib import admin
from .models import Artist
from .models import Movement
from .models import Painting
from .models import MidJourney

admin.site.register(Artist)
admin.site.register(Movement)
admin.site.register(Painting)
admin.site.register(MidJourney)
