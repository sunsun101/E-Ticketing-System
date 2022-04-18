from django.db import models

# Create your models here.

class Seat(models.Model):
    seatNumber = models.TextField()
    seatType = models.TextField()
    seatClass = models.TextField()

class FlightSeat(models.Model):
    BOOKING_STATUS_CHOICES = [
        ("BOOKED", "BOOKED"),
        ("OPEN", "OPEN")
    ]
    fare = models.IntegerField()
    bookingStatus = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default="OPEN")

class Customer(models.Model):
    name = models.TextField()
    email =  models.EmailField()
    mobileNo = models.TextField()
    flightSeat = models.OneToOneField(FlightSeat, on_delete=models.CASCADE)

class Airport(models.Model):
    name = models.TextField()
    address = models.TextField()
    code = models.TextField()

class Flight(models.Model):
    flightNo = models.TextField()
    duration = models.IntegerField()
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_d")
    arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="flight_a")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

class FlightSchedule(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    departureTime = models.DateField()
    gate = models.TextField()

class FlightReservation(models.Model):
    RESERVATION_STATUS_CHOICES = [
        ("CONFIRMED", 'CONFIRMED'),
        ("PENDING", 'PENDING')
    ]
    reservationNumber = models.TextField()
    flight = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE)
    creationDate = models.DateField()
    reservationStatus = models.CharField(max_length=10, choices=RESERVATION_STATUS_CHOICES, default="PENDING")