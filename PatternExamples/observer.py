class WeatherStation:
    def __init__(self):
        self._temp = 0
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def set_temperature(self, temp):
        self._temp = temp
        self._notify()

    def _notify(self):
        for observer in self._observers:
            observer.update(self._temp)

class PhoneApp:
    def update(self, temp):
        print(f"Phone Display: {temp}°C")

class WindowDisplay:
    def update(self, temp):
        print(f"Window Display: {temp}°C")

# Usage: You can add as many displays as you want without touching WeatherStation!
station = WeatherStation()
station.attach(PhoneApp())
station.attach(WindowDisplay())
station.set_temperature(22)