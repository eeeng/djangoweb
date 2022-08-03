from django.urls import path
from . import views
#from django.urls import include

urlpatterns=[
    path('', views.index, name='index'),
    #path('admin/', include(case1.html)),
]
