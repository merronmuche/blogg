from django.contrib import admin

from researches.models import Research

class ResearchAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']
admin.site.register(Research,ResearchAdmin)