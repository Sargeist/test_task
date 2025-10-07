from django.contrib import admin
from .models import Source, Article, Digest, DigestArticle


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'rss_url', 'active')
    search_fields = ('name', 'rss_url')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'published')
    list_filter = ('source',) 
    search_fields = ('title', 'summary', 'link')

class DigestArticleInline(admin.TabularInline):
    model = DigestArticle
    extra = 0

# Админка для дайджестов
@admin.register(Digest)
class DigestAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    inlines = [DigestArticleInline]
