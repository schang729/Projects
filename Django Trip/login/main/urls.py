from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('user/create', views.create),
    path('user/login', views.login),
    path('user/dashboard', views.dashboard),
    path('trips/new', views.newtrip),
    path('trips/create', views.createtrip),
    path('trips/delete/<int:trip_id>', views.deletetrip),
    path('trips/edit/<int:trip_id>', views.editform),
    path('trips/update/<int:trip_id>', views.updatetrip),
    path('trips/<int:trip_id>', views.tripinfo),
    path('trips/join/<int:trip_id>', views.jointrip),
    path('trips/cancel/<int:trip_id>', views.canceltrip),
    path('user/logout', views.logout),
  
    

]