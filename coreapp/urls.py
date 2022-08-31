from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import reverse_lazy


app_name = 'coreapp'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
]