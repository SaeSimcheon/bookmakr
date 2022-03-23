from django.conf.urls import url
from django.urls import path,include

from .views import BookmarkListView,BookmakrCreateView,BookmarkDetailView,BookmarkUpdateView,BookmarkDeleteView

urlpatterns = [
    path('',BookmarkListView.as_view(),name = 'list'),
    path('add/',BookmakrCreateView.as_view(),name = 'add'),
    path('detail/<int:pk>/',BookmarkDetailView.as_view(),name = 'detail'),
    path('update/<int:pk>/',BookmarkUpdateView.as_view(),name = 'update'),
    path('delete/<int:pk>/',BookmarkDeleteView.as_view(),name = 'delete'),
]