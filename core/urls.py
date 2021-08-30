
from core.serializers import GlobalUserSerializer
from django.urls import path, include
from  . import views
from django.conf.urls import url,include



urlpatterns = [
    path('api/register/',views.Register.as_view()),
    path('api/login/', views.Login.as_view()),
    path('api/global_entry/', views.GlobalUserController.as_view()),
    path('api/global_entry/?search_phone=',views.GlobalUserController.as_view()),
    path('api/global_entry/?search_name=',views.GlobalUserController.as_view()),
    path('api/mark_spam/', views.SpamController.as_view())

]

