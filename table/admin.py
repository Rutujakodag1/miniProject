# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Table, Order

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'status')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('table', 'item', 'quantity', 'added_at')
    list_filter = ('table', 'added_at')
