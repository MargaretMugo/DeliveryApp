from django.contrib import admin
from .models import Customer, MenuItem, Category, OrderModel


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'delivery_name', 'quantity')

    def get_urls(self):
        urls = super().get_urls()
        return urls
admin.site.register(Customer)

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)

