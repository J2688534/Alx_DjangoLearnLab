from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in admin list view
    search_fields = ('title', 'author')                     # Search bar functionality
    list_filter = ('publication_year',)                     # Filter options in sidebar

admin.site.register(Book, BookAdmin)

