# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

from machine import Pin,PWM
import time, network 
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("yoyoyo", "aabbcc123")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# servo D1
servo = PWM(Pin(5), freq=50)
servo.duty(30) # 舵機角度設定

def v0_handler(value):
    print(value[0])
    if value[0]=="0":
        servo.duty(30)
        print('大門打開')
    else :
        servo.duty(100)
        print('大門關閉')
    
    
blynk.on("V0", v0_handler)

while True:
    blynk.run()