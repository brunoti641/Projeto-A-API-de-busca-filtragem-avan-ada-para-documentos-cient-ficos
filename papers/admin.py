from django.contrib import admin
from .models import Paper, Author
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_year', 'doi', 'created_at')
    search_fields = ('title','abstract','doi')
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
