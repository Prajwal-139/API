from django.contrib import admin
from .models import BookMyShow

class BookMyShowAdmin(admin.ModelAdmin):
    list_display = ['Mname','Mtime','Mdate','Mticket','Popcorn']

admin.site.register(BookMyShow,BookMyShowAdmin)
