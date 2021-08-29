
from django.urls import path, include
from  . import views
from django.conf.urls import url,include



urlpatterns = [
    path('register/',views.Register.as_view()),
    path('global_entry/', views.GlobalUserController.as_view()),
    path('mark_spam/', views.SpamController.as_view())

]

