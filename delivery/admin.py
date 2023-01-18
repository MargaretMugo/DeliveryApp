from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet

admin.site.site_header = 'Delivery Admin'
admin.site.register(Snippet)
admin.site.unregister(Group)
