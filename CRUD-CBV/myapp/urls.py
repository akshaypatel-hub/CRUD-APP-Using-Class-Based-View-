from django.urls import path
from .views import homeView,UpdateView,DeleteView

urlpatterns = [
    path('home/',homeView.as_view(),name="home"),
    path('home/update/<int:pk>', UpdateView.as_view(), name="update"),
    path('home/delete/<int:pk>', DeleteView.as_view(), name="delete"),
]
