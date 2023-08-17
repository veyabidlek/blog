
from django.urls import path
from. import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name="create"),
    path('<int:pk>', views.newsDetailView.as_view(), name='newsDetail'),
    path('<int:pk>/update', views.newsUpdateView.as_view(), name='newsUpdate')
]


