from django.contrib import admin

# Register your models here.

from core.models import Language,Catagory,Notes

admin.site.register(Language)
admin.site.register(Catagory)
admin.site.register(Notes)