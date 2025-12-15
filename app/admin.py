from django.contrib import admin
from .models import *
from django.contrib import admin


admin.site.register(Genero)
admin.site.register(Episodio)
admin.site.register(Temporada)
admin.site.register(Pais)
admin.site.register(Ator)

class EpisodioInline(admin.TabularInline):
    model = Episodio
    extra = 1

class PaisInline(admin.TabularInline):
    model = Pais
    extra = 1

class AtorInline(admin.TabularInline):
    model = Ator
    extra = 1

class FilmeInline(admin.TabularInline):
    model = Filme
    extra = 1

class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [EpisodioInline]

class ContinenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PaisInline]

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AtorInline]

class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [FilmeInline]

admin.site.register(Serie, SerieAdmin)
admin.site.register(Continente, ContinenteAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Diretor, DiretorAdmin)