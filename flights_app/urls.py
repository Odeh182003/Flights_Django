from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("<int:id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book"),
]