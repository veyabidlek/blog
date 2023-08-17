from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, ListView, UpdateView
# Create your views here.
def news_home(request):
  news = Articles.objects.order_by('-date')
  return render(request, 'news/home.html', {'news':news})

class newsDetailView(DetailView):
  model = Articles
  template_name = 'news/details_view.html'
  context_object_name = 'article'


class newsUpdateView(UpdateView):
  model = Articles
  template_name='news/create.html'
  fields=['title','anons','fullText','date']
  
  
  
def create(request):
  error=''
  if request.method == "POST":
    form = ArticlesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('news_home')
    else:
      error='Incorrect Input'
  form = ArticlesForm()
  data={
    'form':form,
    'error':error
  }
  return render(request, 'news/create.html', data)