from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet

admin.site.site_header = 'Delivery Admin'


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)


admin.site.register(Snippet)
admin.site.unregister(Group)
