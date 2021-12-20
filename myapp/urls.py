from django.urls import path
from .views import  ThanksTemplateView ,AccountCreateView ,AccountDetailView,AccountUpdateView,AccountDeleteView,AccountlistView

urlpatterns = [

    path('',AccountlistView.as_view(),name="list"),
    path('create/',AccountCreateView.as_view(),name="Create"),
    path('update/<int:pk>', AccountUpdateView.as_view(), name="Update"),
    path('detail/<int:pk>',AccountDetailView.as_view(),name="Details"),
    path('delete/<int:pk>',AccountDeleteView.as_view(),name="Delete"),
    path('thankyou/',ThanksTemplateView.as_view(),name="thanks"),


]