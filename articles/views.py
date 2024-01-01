from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model  = Article
    template_name  = 'article_detail.html'


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

class ArticleCreateVeiw(UserPassesTestMixin, LoginRequiredMixin,CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ('title','summary','body','photo','author',)

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser



class Search(ListView):
    template_name = 'article_list.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        return  Article.objects.filter(title__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, * , object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

