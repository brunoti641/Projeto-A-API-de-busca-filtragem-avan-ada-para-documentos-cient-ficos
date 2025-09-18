from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    def __str__(self):
        return self.name
class Paper(models.Model):
    title = models.CharField(max_length=1000)
    abstract = models.TextField(blank=True)
    body = models.TextField(blank=True)
    published_year = models.PositiveSmallIntegerField(db_index=True, null=True, blank=True)
    doi = models.CharField(max_length=255, unique=True, null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='papers', blank=True)
    keywords = models.JSONField(default=list, blank=True)
    xml_raw = models.TextField(blank=True)  # store raw xml if needed
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title[:80]
