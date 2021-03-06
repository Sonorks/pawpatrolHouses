from django.urls import path

from . import views

urlpatterns = [
    path('v1/homes/search/', views.getAllHomes, name='homes'),
    path('v1/homes/<searchCity>', views.getHomesByCity, name='searchHomes'),
    path('v1/homes/booking/', views.addBooking, name="booking"),
    path('v1/homes/myBooking/', views.getBookingsByUser, name = "getBooking"),
    path('v1/homes/removeBooking/', views.removeBooking, name ="removeBooking"),
]