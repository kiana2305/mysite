from django.contrib import admin
from website.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email', 'created_date')
    search_fields = ('name', 'massage')
admin.site.register(Contact,ContactAdmin)
