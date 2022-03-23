# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from audioop import reverse

from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
# Create your views here.

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmakrCreateView(CreateView):
    model=Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model=Bookmark
    fields = ['site_name','url']
    
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

