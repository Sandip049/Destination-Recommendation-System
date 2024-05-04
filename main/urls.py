from django.urls import path
from django.urls import include
from . import views

from registration.views import profile_editpage 

urlpatterns = [
     
    ## path('', views.mainpageview, name="mainpage"),
     path('', include('destination.urls')),
path('profile/', views.profilepage, name='profilepage'),
path('profile/user_profile_edit/', profile_editpage ,name='edit_profile'),
path('places/', views.Searchplace.as_view() ,name='places'),
]
