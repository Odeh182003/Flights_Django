from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Flight,Passenger,Airport
from .agent import run_ai_agent
from .forms import FlightForm, PassengerForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django_q.tasks import Task, async_task
from .signals import flight_booked
from django.contrib import messages
def is_admin(user):
    return user.is_superuser or user.groups.filter(name='Admin').exists()
def is_passenger_or_admin(user):
    return user.is_authenticated

# Create your views here.
@login_required(login_url='/users/login/')
def flight_index(request):
    return render(request, "flights/index.html",{
        "flights":Flight.objects.all()
    })
@login_required(login_url='/users/login/')
def flight(request,id):
    flight = Flight.objects.get(pk=id)
    return render(request, "flights/flight.html",{
        "flight":flight,
        "passengers":flight.passenger.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    })

@login_required(login_url='/users/login/')
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        flight_booked.send(sender=book, flight=flight, passenger=passenger)  # Trigger the signal
        messages.success(request, f"Successfully booked {passenger} on flight to {flight.destination}!")
        return HttpResponseRedirect(reverse("flights_app:flight", args=[flight.id]))
    
@login_required(login_url='/users/login/')
def cancel(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.remove(flight)
        messages.success(request, f"Successfully cancelled booking for {passenger} on flight to {flight.destination}!")
        return HttpResponseRedirect(reverse("flights_app:flight",args=[flight.id]))
    
@login_required(login_url='/users/login/')
def ai_chat_view(request):
   # ai_response = None
   # user_query = None
    if request.method == "POST":
        user_query = request.POST.get('user_query')
# Async task to process the AI query in the background instead of blocking the request
#(instead of running the AI agent synchronously which can take time and block the request)
        task_id = async_task('flights_app.tasks.process_ai_query_task', user_query)
       # ai_response = run_ai_agent(user_query)
        return render(request, "flights/chat.html", {
            "user_query": user_query,
            "task_id": task_id,
             "processing": True,
        })
    return render(request, "flights/chat.html")

#Ran the Worker: Started a separate background worker process via 
# python manage.py qcluster 
# to listen for and execute queued tasks.

@login_required(login_url='/users/login/')
def check_ai_task_status(request, task_id):
  #  """API endpoint to check if the background task is done and fetch the result."""
    task_entry = Task.objects.filter(id=task_id).first()
    
    if not task_entry:
        return JsonResponse({"status": "processing"})
    
    if task_entry.success:
        return JsonResponse({
            "status": "completed",
            "ai_response": task_entry.result
        })
    else:
        return JsonResponse({
            "status": "failed",
            "ai_response": "The AI task encountered an error while processing."
        })
    
@login_required(login_url='/users/login/')
def dashboard(request):
    airports = Airport.objects.all()
    passengers = Passenger.objects.all()
    return render(request,"flights/dashboard.html",{
        "airports": airports,
        "passengers": passengers
    })

@user_passes_test(is_admin, login_url='/users/login/')
def add_flight(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("flights_app:flight_index"))
    else:
        form = FlightForm()
    return render(request, "flights/add_flight.html", {"form": form})

@user_passes_test(is_admin, login_url='/users/login/')
def add_passenger(request):
    if request.method == "POST":
        form = PassengerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("flights_app:flight_index"))
    else:
        form = PassengerForm()
    return render(request, "flights/add_passenger.html", {"form": form})

