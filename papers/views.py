from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from rest_framework import generics
from .models import Paper
from .serializers import PaperSerializer
from .filters import PaperFilter
class PaperSearchView(generics.ListAPIView):
    serializer_class = PaperSerializer
    filterset_class = PaperFilter
    def get_queryset(self):
        qs = Paper.objects.all().prefetch_related('authors')
        q = self.request.query_params.get('q', None)
        if q:
            # If running on SQLite, Postgres search helpers will not work;
            # fallback to icontains search across fields for local testing.
            try:
                vector = SearchVector('title','abstract','body')
                query = SearchQuery(q)
                qs = qs.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.1).order_by('-rank')
            except Exception:
                # simple fallback
                qs = qs.filter(title__icontains=q) | qs.filter(abstract__icontains=q) | qs.filter(body__icontains=q)
        return qs
