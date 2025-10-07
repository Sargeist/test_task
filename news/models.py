from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=200)
    rss_url = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=400)
    link = models.URLField(unique=True, db_index=True)
    published = models.DateTimeField(db_index=True)
    summary = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
class Digest(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class DigestArticle(models.Model):
    digest = models.ForeignKey(Digest, on_delete=models.CASCADE, related_name='digest_articles')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='+')
    
    class Meta:
        unique_together = ('digest', 'article')
        
    def __str__(self):
        return f"{self.digest.name} - {self.article.title}"