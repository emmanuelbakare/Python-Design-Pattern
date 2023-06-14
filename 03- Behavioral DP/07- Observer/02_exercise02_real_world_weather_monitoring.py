from abc import ABC, abstractmethod

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._weather_data = {}


    def attach(self, observer): # subscribe for notification
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_weather(self, temperature, humidity, pressure):
        self._weather_data['temperature'] = temperature
        self._weather_data['humidity'] = humidity
        self._weather_data['pressure'] = pressure
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._weather_data)

class Observer(ABC):
    @abstractmethod
    def update(self, weather_data):
        pass

class DisplayDevice(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, weather_data):
        print("sending to:",self._name)
        print(f"{self._name} - Temperature: {weather_data['temperature']}°C, Humidity: {weather_data['humidity']}%, Pressure: {weather_data['pressure']} hPa")

class PrintDevice(Observer):
    
    def update(self, weather_data):
        print("Sending to printer...")
        for data in weather_data:
            print(f"{data}: {weather_data[data]}")


#usage

weather_station = WeatherStation()


#observer
display1 = DisplayDevice("Living Room Display")
display2 = DisplayDevice("Bed Room Display")
printer = PrintDevice()


weather_station.attach(display1)
weather_station.attach(display2)
weather_station.attach(printer) 


weather_station.set_weather(25, 70, 1010) 


weather_station.detach(printer)
weather_station.detach(display2)
print()
weather_station.set_weather(20, 60, 1003)


