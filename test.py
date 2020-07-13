import pyowm

owm = pyowm.OWM('0e906c8c7e7702e2088321df365e4ed5')

mgr = owm.weather_manager()

place = input("Введите город: ")
observation = mgr.weather_at_place(place)

weather = observation.weather

print(observation.weather.temperature('celsius')['temp'], "\n")
print(weather.detailed_status)