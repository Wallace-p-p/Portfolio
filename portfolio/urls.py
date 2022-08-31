from django.contrib import admin
from django.urls import path
from coreapp import views as v
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coreapp/', include('coreapp.urls')),
    path('', v.MainView.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]