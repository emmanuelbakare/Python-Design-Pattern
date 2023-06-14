#classes  
#object that contains the time  that flights are are available
#each Schedule is attached to flight
from datetime import datetime

class Schedule:
    def __init__(self, name, depart, arrive):
        self.name = name
        self.depart= depart
        self.arrive= arrive

    def to_date(self, val):
        try:
            return datetime.strptime(val, "%d/%m/%Y %H:%M")
        except:
            return None
        
    def date_diff(self):
        
        datediff= self.to_date(self.arrive) - self.to_date(self.depart)
        return datediff


# a flight object that takes in the destinations and a schedule    
class Flight:
    def __init__(self, flight_id, depart_from, arrive_at, schedule=None):
        self.flight_id = flight_id
        self.depart_from = depart_from
        self.arrive_at = arrive_at
        self.schedule = schedule

    def assign_schedule(self, schedule):
        self.schedule = schedule

        
    def info(self):
        print(f'''
        Flight Name: {self.flight_id}
        Departure Time:{self.depart_from}({self.schedule.depart})
        Arrival Time: {self.arrive_at}({self.schedule.arrive})
        Time Difference: {self.schedule.date_diff() } days''')


# Object is used to book a flight, add a price and assign a seat    
class Booking:  #originator
    # def __init__(self, name, flight=None, price = None):
    def __init__(self, name, flight, price, seat=None):
        self.name = name 
        self.flight = flight 
        self.price = price
        self.seat = seat

    def get_price(self):
        return self.price
    
    def get_flight(self):
        return self.flight 
    
    def set_seat(self, seat):
        self.seat = seat

    def get_seat(self):
        return self.seat
    
     # if status = True (Flight is booked),
    # if status = False (Flight is on_hold)
    def book_flight(self,status=True): #create memento
        return BookedFlight(self,status)
        

    def restore_booking(self, booking):
        self.name = booking.get_name()
        self.flight = booking.get_flight()  
        self.price = booking.get_price()
        self.seat = booking.get_seat()


#The Memento
class BookedFlight: #memento
    def __init__(self, booking, status=True):
        self.booking = booking
        self.status = status
    
    def get_booking(self):
        return self.booking 
    
    def get_status(self):
        return self.status
    

class FlightManager:  # Caretaker 
    def __init__(self):
        self.flight_statuses = []

    def set_booked_flight(self, booked_flight):  
        self.flight_statuses.append(booked_flight)
    
    def restore_booked_flight(self, index):
        return self.flight_statuses[index]
    
    def get_booking_index(self, booking):
        for num,flight in enumerate(self.flight_statuses):
            if flight.booking == booking:
                return num
        return None
    

    def onhold_bookings(self):
        bookings =[bf.booking for bf in self.flight_statuses if not bf.status] 
        return bookings
    
    def approved_bookings(self):
        bookings = [bf.booking for bf in self.flight_statuses if bf.status]  
        return bookings
    
    def approve_booking(self, booking, status=True):
        index=self.get_booking_index(booking)
        if index is not None:
            flight_booking = self.flight_statuses[index]
            flight_booking.status = status

    def cancel_booking(self, booking):
        index= self.get_booking_index(booking)
        self.flight_statuses.pop(index)

    #get manifest
    def get_booking_manifest(self,flight):
        bookings = [fs.booking for fs in self.flight_statuses if fs.booking.flight == flight]
        return bookings
    
    # get manifest passengers only
    def get_passengers_manifest(self, flight):
        passengers = [fs.booking.name for fs in self.flight_statuses if fs.booking.flight == flight]
        return passengers
    
    def flight_info(self, bookings):
            info = ""
            # List of booked lights object
            for booking in bookings:
                flight = booking.flight
                info += f"Name: {booking.name}\n"
                info += f"Flight name: {flight.flight_id}\n"
                info += f"From : {flight.depart_from} \n"
                info += f"To : {flight.arrive_at}\n"
                info += f"=SCHEDULE:\n"
                info += f"Flight: {flight.schedule.name}\n"
                info += f"Departure Time: {flight.schedule.depart}\n"
                info += f"Arrive Time: {flight.schedule.arrive}\n"
                info += f"Duration: {flight.schedule.date_diff()}  \n"
                info += f"*"*30+"\n"
            print(info)



#Client Code - Usage 

def heading(text):
        print(text.upper())
        print("-"*len(text))


morning1 = Schedule("Morning 1", "05/09/2024 09:30","05/09/2024 15:25")
morning2= Schedule("Morning 2", "06/09/2024 11:00","07/09/2024 16:30")
afternoon1= Schedule("Afternoon 1", "05/09/2024 13:00","7/09/2024 14:30")

#Flight
flight1 = Flight("FG983", "Johannesburge","Lagos")
flight2 = Flight("IYK392", "Lagos","Abidjan")
flight3 = Flight("ABC900", "Abuja","London")

flight1.assign_schedule(morning1)
flight2.assign_schedule(afternoon1)
flight3.assign_schedule(morning2)


booking1 = Booking("Emmanuel", flight2,195)
booking2 = Booking("Deji", flight2,33)
booking3 = Booking("Lizzy", flight1,23)
booking4 = Booking("Janet", flight3,165)
booking5 = Booking("Bunmi", flight3,33)


agent = FlightManager() #Caretaker
agent.set_booked_flight(booking1.book_flight())
agent.set_booked_flight(booking2.book_flight(False))
agent.set_booked_flight(booking3.book_flight())
agent.set_booked_flight(booking4.book_flight(False))
agent.set_booked_flight(booking5.book_flight())


#--- Retrieve Manifest, Passengers on a flight
flight = flight1
passengers=agent.get_passengers_manifest(flight)
print(f"Flight: {flight.flight_id} ({flight.depart_from} to {flight.arrive_at}) has {len(passengers)} passenger(s): ")
print(passengers) 
print()


#--- Confirm/Unconfirm a booking 
# agent.approve_booking(booking1, False)

#--- Cancel Booking
# agent.cancel_booking(booking4)
# agent.cancel_booking(booking1)


# heading('ON HOLD BOOKINGS')
# agent.flight_info(agent.onhold_bookings()) 


heading('APPROVED BOOKINGS')
agent.flight_info(agent.approved_bookings())