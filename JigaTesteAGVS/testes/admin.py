from django.contrib import admin

from . import models
# Register your models here.
class TestesAdmin(admin.ModelAdmin):
    pass

class PlacasAdmin(admin.ModelAdmin):
    list_display=("NOME",)
    
class PropriedadesAdmin(admin.ModelAdmin):
    pass

class TiposAdmin(admin.ModelAdmin):
    list_display=("NOME","COD")

admin.site.register(models.tbTestes, admin_class=TestesAdmin)
admin.site.register(models.tbPlacas, PlacasAdmin)
admin.site.register(models.tbPropriedades, PropriedadesAdmin)
admin.site.register(models.tbTipos, TiposAdmin)