from django.contrib import admin
from .models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'delivery_name', 'license_plate')

    def get_urls(self):
        urls = super().get_urls()
        return urls


admin.site.register(Driver)
