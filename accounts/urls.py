from django.urls import path,re_path
from accounts.views import SignUp,CreateProfile,DetailProfile,HomePage
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns=[
    path('signup/',SignUp.as_view(template_name='accounts/signup.html'),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('<slug:username>/profile/create', CreateProfile.as_view(), name='createprofile'),
    path('<slug:username>/profile/<int:pk>/', DetailProfile.as_view(), name='profile'),
    path('homepage/',HomePage.as_view(),name='HomePage'),
    path('<slug:username>/profile/',DetailProfile , name='verifyprofile'),
]