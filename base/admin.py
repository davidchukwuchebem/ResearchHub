from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_at')
    search_fields = ('title', 'abstract', 'author__username')
    list_filter = ('category', 'published_at')
