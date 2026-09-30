from django.urls import path
from . import views

#app_name="flights_app"
urlpatterns = [
#Django maps URL Paths to Python callback functions ("views") 
#The strings use parameter tag to "capture" values from the URLs
#when a user requests a page Django runs through each path in order 
# and stops when it finds the first match that matches the request
#if none of them match Django calls a special-case 404 view.
#once one of the URL paths matches Django calls the given view which is python function
    path("",views.flight_index,name="flight_index"),
    path("<int:id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book"),
    path("<int:flight_id>/cancel",views.cancel,name="cancel"),
    path("chat", views.ai_chat_view, name="chat"),
    path("dashboard", views.dashboard, name="dashboard")
]