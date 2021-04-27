from django.urls import path
from . import views


urlpatterns = [
    path('crud', views.index, name='index'),
    # path('signup/', views.signup),
]
