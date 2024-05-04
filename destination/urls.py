from django.urls import path
from . import views
from destination.views import Rateview

urlpatterns = [
    path('',views.placelistview.as_view(), name='placelist'),
    path('<int:pk>/', views.placedetailview, name='placeview'),
    path('rate/<int:r_id>/',Rateview,name='rate-place'),
   # path('celery/', test , name='celery'),
    
]