from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('user/<str:username>/', views.user_profile_view, name='user_profile'),
    path('users/', views.UserListViewCB.as_view(), name='lista_users'),
    path('cerca/', views.cerca, name='funzione_cerca')
    ]
