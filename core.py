import requests
import gpiozero
import time

url = "https://everypixel-api.p.rapidapi.com/keywords"

querystring = {"url":"https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F_Od0_3vFBzHY%2FTJechRB6evI%2FAAAAAAAAAAM%2F3PKnboxFuTU%2Fs1600%2FPlasticBottle-PET.jpg&f=1&nofb=1"}

headers = {
    'x-rapidapi-host': "everypixel-api.p.rapidapi.com",
    'x-rapidapi-key': "e3d62ccdd0msh21ca55e32a57499p194bbfjsn26247a89830c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

results = dict()

def parse_text(text):
    resp = text
    resp = resp[13:]
    i = 0
    j = 0
    symb = ''
    keyword = ''
    score = ''

    while i < len(resp):
        if resp[i] == 'k':
            j = i + 10
            if j < len(resp):
                symb = resp[j]
            else:
                break
            
            while symb != '"' and j < len(resp):
                keyword += symb
                j += 1
                symb = resp[j]
                
            j += 10
            while symb != '}' and j < len(resp):
                symb = resp[j]
                score += symb
                j += 1
                symb = resp[j]
                
            results[keyword] = float(score)
            score = ''
            keyword = ''
            i = j
        i += 1

parse_text(response.text)

servo1 = gpiozero.AngularServo(17, min_angle = -90, max_angle = 90)#right platform servo
servo1.angle = 0
servo2 = gpiozero.AngularServo(18, min_angle = -90, max_angle = 90)#left platform servo
servo2.angle = 0

sensor = gpiozero.MotionSensor(4)
led = gpiozero.LED(14)

"""while True:
    if sensor.motion_detected():            
        led.on()
        #photo
        querystring = {"url":"https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F_Od0_3vFBzHY%2FTJechRB6evI%2FAAAAAAAAAAM%2F3PKnboxFuTU%2Fs1600%2FPlasticBottle-PET.jpg&f=1&nofb=1"}        
        response = requests.request("GET", url, headers=headers, params=querystring)
        if "Bottle" in results.keys() and "Plastic" in results.keys():
            servo1.angle = -90
            servo2.angle = 90
            time.sleep(2)
            servo1.angle = 0
            servo2.angle = 0
            print(123)
        else:
            servo1.angle = 90
            servo2.angle =-90
            time.sleep(2)
            servo1.angle = 0
            servo2.angle = 0"""
         
print(results.keys())

results.clear()
