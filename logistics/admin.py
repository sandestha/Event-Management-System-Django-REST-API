from django.contrib import admin
from .models import Catering, Equipment, Transportation

# Register your models here.
admin.site.register(Catering)
admin.site.register(Equipment)
admin.site.register(Transportation)