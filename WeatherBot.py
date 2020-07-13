import telebot
import pyowm

bot = telebot.TeleBot("1393564486:AAERtc2-Z9mRvjqaQR83PdWYCfqo_mc9yvc")
owm = pyowm.OWM('0e906c8c7e7702e2088321df365e4ed5')

mgr = owm.weather_manager()

@bot.message_handler(commands=['start', 'help'])
def start(message):
	bot.send_message(message.chat.id, "Hello! \n I am WeatherBot and I can tell you temperature in your city. \n So, you can just type your city name.")
@bot.message_handler(content_types=['text'])
def send_welcome(message):
	observation = mgr.weather_at_place(message.text)
	weather = observation.weather
	temp = weather.temperature('celsius')["temp"]

	answer = str("There is " + weather.detailed_status + " in " + message.text + " now \n")
	answer += str("Temperature is " + str(temp) + " degrees \n")
	bot.send_message(message.chat.id, answer)


bot.polling( none_stop = True)