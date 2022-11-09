from django.contrib import admin

from researches.models import Research, User

class ResearchAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'image',]
admin.site.register(Research,ResearchAdmin)

class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'firstname', 'lastname', 'email']

admin.site.register(User, UserAdmin)