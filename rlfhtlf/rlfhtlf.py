import serial
import time as t
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv(verbose=True)
email_address = os.getenv('MY_EMAIL_ADDRESS')
email_password = os.getenv('MY_EMAIL_PASSWORD')
email_address_to = os.getenv('TO_EMAIL_ADDRESS')

subject_content = [
# 물류센터 도착시 발송
["고객님의 소중한 상품을 실을 차량이 물류센터에 도착하였습니다.", # 제목
"3조 운송이 고객님의 소중한 상품을 차량에 싣고 배달지를 향해 출발합니다."], # 내용
# 경유지1 도착시 발송
["고객님의 소중한 상품을 실은 차량이 경유지1에 도착하였습니다.", # 제목
"고객님의 소중한 상품이 경유지1을 지나고 있습니다."], # 내용
# 경유지2 도착시 발송
["고객님의 소중한 상품을 실은 차량이 경유지2에 도착하였습니다.", # 제목
"고객님의 소중한 상품이 경유지2를 지나고 있습니다."], # 내용
# 배달지 도착시 발송
["고객님의 소중한 상품이 배달지에 도착하였습니다.", # 제목
"3조 운송이 고객님의 소중한 상품을 배달 완료하였습니다."]] # 내용

def sendEmail(i):
    msg = EmailMessage()
    msg['Subject'] = subject_content[i][0]
    msg['From'] = email_address
    msg['To']= email_address_to
    msg.set_content(subject_content[i][1])

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_address,email_password)
        smtp.send_message(msg)
        smtp.quit()

#mobilerobotSerial = serial.Serial('COM5', 9600, timeout=1)
#manipulatorSerial = serial.Serial('COM11',9600,timeout=1)

sendEmail(0)
'''
while True:
    line = mobilerobotSerial.readline().decode("utf-8")
    
    if line == "logistics_arrived":
        sendEmail(0)
        print("ok")

    if line == "waypoint1_arrived":
        sendEmail(1)
        print("ok11")

    if line == "waypoint2_arrived":
        sendEmail(2)

    if line == "delivery_finished":
       sendEmail(3)
    
    # Python 3.10버전 이상부터 지원됩니다.
    match line:
        case "logistics_arrived":
            manipulatorSerial.write("run")
            sendEmail(0)
        case "waypoint1_arrived":
            print("waypoint1_arrived")
            sendEmail(1)
        case "waypoint2_arrived":
            print("waypoint2_arrived")
            sendEmail(2)
        case "delivery_finished":
            print("waypoint2_arrived")
            sendEmail(3)
            '''
    #if line == "findbox":
        #manipulatorSerial.write("pickupbox")