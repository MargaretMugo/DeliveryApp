from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html

admin.site.site_header = 'Delivery App'


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'font_size_html_display')
    list_filter = ('created',)
    change_list_template = 'admin/deliveries/delivery_change_list.html'

    readonly_fields = ('body_preview',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>', self.change_font_size)
        ]
        return custom_urls + urls

    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'font size set successfully!')
        return HttpResponseRedirect("../")

    def font_size_html_display(self, obj):
        display_size = obj.font_size if obj.font_size <= 30 else 30
        return format_html(
            f'<span style="font-size: {display_size}px;">{obj.font_size}</span>'
        )


admin.site.register(Snippet)
admin.site.unregister(Group)
