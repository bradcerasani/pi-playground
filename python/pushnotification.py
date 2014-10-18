import time
import Adafruit_MCP9808.MCP9808 as MCP9808
import httplib, urllib

# Temperature sstuff
# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Default constructor will use the default I2C address (0x18) and pick a default I2C bus.
sensor = MCP9808.MCP9808()

# Initialize communication with the sensor.
sensor.begin()
temp = sensor.readTempC()
lastTemp = 0
var = 'Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp))

# Application specific variables
application_token = "aqXxR8tiaKy8Q9hLQKCbwwSysnrAhU"
user_token = "ufqBkUqEwtq8XVbx8q2cjKqnADvNwh"

# Message specific variables
title = "Warning!"
message = var
url = "http://google.com"
# To remove any of these fields you will need to remove them
# from the conn.request() below

while True : 
	temp = sensor.readTempC()
	print temp
	if (temp > 26.8 and lastTemp <26.8) :
		print "too hot"
		# Start your connection with the Pushover API server
		conn = httplib.HTTPSConnection("api.pushover.net:443")

		# Send a POST request in urlencoded json
		conn.request("POST", "/1/messages.json",
		urllib.urlencode({
		"token": application_token,
		"user": user_token,
		"title": title,
		"message": message,
		"url": url,
		}), { "Content-type": "application/x-www-form-urlencoded" })

		# Listen for any error messages or other responses
		conn.getresponse()

	time.sleep(0.05)
	lastTemp = temp

# var = raw_input("Please enter something:")
