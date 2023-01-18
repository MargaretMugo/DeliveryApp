from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet

admin.site.site_header = 'Delivery Admin'


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)
    change_list_template = 'admin/deliveries/delivery_change_list.html'


admin.site.register(Snippet)
admin.site.unregister(Group)
