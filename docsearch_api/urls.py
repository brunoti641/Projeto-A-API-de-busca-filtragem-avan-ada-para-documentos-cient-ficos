from django.urls import path, include
from django.contrib import admin
from papers.views import PaperSearchView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/papers/', PaperSearchView.as_view(), name='paper-search'),
]
