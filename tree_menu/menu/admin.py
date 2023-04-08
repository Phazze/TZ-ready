from django.contrib import admin
from .models import Menu, MainMenu


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ('name', 'name_slug', 'menu', 'parent')
    list_filter = ('name',)
    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or level",
            'fields': (('menu', 'parent'), 'name', 'name_slug')
        }),
    )
    prepopulated_fields = {"name_slug": ('name',)}


@admin.register(MainMenu)
class AdminMainMenu(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {"slug": ('title',)}
