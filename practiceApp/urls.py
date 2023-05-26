from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .views import home, post, category

urlpatterns = [
    path('', home),
    # path('', about),
    path('<slug:url>', post),
    path('category/<slug:url>', category)   
]
