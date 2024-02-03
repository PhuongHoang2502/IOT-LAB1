from adafruit_mqtt import Adafruit_MQTT
import time
import random

device1 = Adafruit_MQTT()

counter = 10
while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        # todo
        print("Random data is publishing...")
        temp = random.randint(25, 40)
        device1.publish("cambien1", temp)
        light = random.randint(100, 500)
        device1.publish("cambien2", light)
        humi = random.randint(40, 85)
        device1.publish("cambien3", humi)
    time.sleep(1)
