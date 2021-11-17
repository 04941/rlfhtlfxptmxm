import serial
import pyautogui
import time as t

kakao_content = [
# 물류센터 도착시 발송
"3wh dnsthddl rhrorsladml thwndgks tkdvnadmf ckfiddp tlerh qoekfwlfmf gidgo cnfqkfgkqslek.",
# 경유지1 도착시 발송
"rhrorsladml thwndgks tkdvnadl ruddbwl1dmf wlskrh dlTtmqslek.",
# 경유지2 도착시 발송
"rhrorsladml thwndgks tkdvnadl ruddbwl2fmf wlskrh dlTtmqslek.",
# 배달지 도착시 발송
"3wh dnsthddl rhrorsladml thwndgks tkdvnadmf qoekf dhksfygkduTtmqslek."]

def sendkakao(i):
    pyautogui.click(x=763, y=1061) # 하단 바 카카오톡 클릭
    pyautogui.click(x=705, y=691) # 카카오톡 채팅창 클릭
    pyautogui.typewrite(kakao_content[i]) # 메시지 입력
    t.sleep(1)
    pyautogui.click(x=964, y=697) # 전송 버튼 클릭

sendkakao(1)

mobilerobotSerial = serial.Serial('COM5', 9600, timeout=1)
#manipulatorSerial = serial.Serial('COM11',9600,timeout=1)

while True:
    line = mobilerobotSerial.readline().decode("utf-8")
    
    if line == "logistics_arrived":
        sendkakao(1)
        print("ok")

    if line == "waypoint1_arrived":
        sendkakao(1)
        print("ok11")

    if line == "waypoint2_arrived":
        sendkakao(1)

    if line == "delivery_finished":
       sendkakao(1)

    #if line == "findbox":
        #manipulatorSerial.write("pickupbox")

'''t.sleep(10)

pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=964, y=697)

x, y = pyautogui.position()  
print('x={0}, y={1}'.format(x, y))
'''