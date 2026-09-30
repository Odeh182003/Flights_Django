from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight,Passenger,Airport
from .agent import run_ai_agent
# Create your views here.
def flight_index(request):
    return render(request, "flights/index.html",{
        "flights":Flight.objects.all()
    })
def flight(request,id):
    flight = Flight.objects.get(pk=id)
    return render(request, "flights/flight.html",{
        "flight":flight,
        "passengers":flight.passenger.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    })
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=[flight.id]))
def cancel(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.remove(flight)
        return HttpResponseRedirect(reverse("flight",args=[flight.id]))
def ai_chat_view(request):
   # ai_response = None
   # user_query = None
    if request.method == "POST":
        user_query = request.POST.get('user_query')
        ai_response = run_ai_agent(user_query)
        return render(request, "flights/chat.html",{#context
            "user_query": user_query,
            "ai_response": ai_response
        })
    return render(request, "flights/chat.html")
def dashboard(request):
    airports = Airport.objects.all()
    passengers = Passenger.objects.all()
    return render(request,"flights/dashboard.html",{
        "airports": airports,
        "passengers": passengers
    })