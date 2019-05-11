from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('<int:pk>/', views.UserDetail.as_view(), name="users-detail"),
    path('', views.UserList.as_view(), name="users-list"),
    path('login/', views.UserLogin.as_view(), name='users-login'),
    path('signup/', views.CreateClient.as_view(), name='cleint-signup'),
    # path('profile/', views.UserLogin.as_view(), name='users-login'),
]
