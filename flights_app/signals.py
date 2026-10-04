from django.dispatch import Signal, receiver
#Signal(providing_args=["flight", "passenger"])
flight_booked = Signal()

@receiver(flight_booked)
def flight_booked_handler(sender, **kwargs):
    passenger = kwargs.get('passenger')
    flight = kwargs.get('flight')
    
    print(f"--- SIGNAL TRIGGERED ---")
    print(f"Passenger: {passenger} successfully booked Flight ID: {flight.id} ({flight.origin} -> {flight.destination})")
    print(f"------------------------")