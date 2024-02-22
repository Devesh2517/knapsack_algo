from django.contrib import admin
from .models import *
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id','name','price','description']

    
admin.site.register(Item,ItemAdmin)