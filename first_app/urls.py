from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit,name='edit'),
    path('profile/changepassword',views.changepass,name='change_pass'),
    path('profile/changepassword2',views.changepass_2,name='change_pass_2'),
]