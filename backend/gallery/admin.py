from django.contrib import admin
from .models import Gallery, Photo


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """галерея"""
    list_display = ('name', 'created', 'id')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """photo"""
    list_display = ('name', 'created', 'id')
    prepopulated_fields = {'slug': ('name',)}