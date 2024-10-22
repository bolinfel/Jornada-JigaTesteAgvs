from django.contrib import admin
from . import models

class TestesAdmin(admin.ModelAdmin):
    pass

class PlacasAdmin(admin.ModelAdmin):
    list_display=("NOME",)
    
class PropriedadesAdmin(admin.ModelAdmin):
    list_display=("FK_PLACA","DESCRICAO")

class TiposAdmin(admin.ModelAdmin):
    list_display=("NOME","COD")

admin.site.register(models.tbTestes, admin_class=TestesAdmin)
admin.site.register(models.tbPlacas, PlacasAdmin)
admin.site.register(models.tbPropriedades, PropriedadesAdmin)
admin.site.register(models.tbTipos, TiposAdmin)