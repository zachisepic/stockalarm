
import alpaca_trade_api as alp
import datetime
from playsound import playsound
import cv2 as cv
from tkinter import Tk, messagebox
import random
import pandas as pd
import os



df = pd.read_excel("company_list.xlsx")
symbols = df["Symbol"].values.tolist()

key = input("your alpaca key: ")
seckey = input("your secret alpaca key: ")

url = "https://paper-api.alpaca.markets"

api = alp.REST(key, seckey, url, api_version="v2")

account = api.get_account()

alarmhour = int(input("what hour: "))
alarmmin = int(input("what minute: "))
alarmam = input("am/pm: ")



randomright = symbols[random.randrange(0,len(symbols))]
randomleft = symbols[random.randrange(0,len(symbols))]

print(randomleft, randomright)



if alarmam == "pm":
    alarmhour += 12


leftbool = False
rightbool = False







while True:
    if alarmhour==datetime.datetime.now().hour and alarmmin ==datetime.datetime.now().minute:
        print("wake up")
        playsound("D:\game\stock\\alarm.mp3")
        #!(face_detector)
        capture = cv.VideoCapture(0) #to open Camera
        pretrained_model = cv.CascadeClassifier("face_detector.xml") 
        while True:
            boolean, frame = capture.read()
            if boolean == True:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) 
                
                # drawing rectangle in frame
                for (x,y,w,h) in coordinate_list:
                    cv.rectangle(frame, (x,y), (x+w, y+h), (255,50,0), 2)
                    
                    
                    

                    if x >= 250 and leftbool == False:
                        print("left")
                        leftbool = True
                        rightbool = True
                        ordor = api.submit_order(symbol=randomleft,qty=5,side="buy",type="market",time_in_force="day")
                        messagebox.askokcancel(randomleft)
                          
                
                        
                       
                    if x <= 250 and rightbool == False:
                        print("right")
                        rightbool = True
                        leftbool = True
                        ordor = api.submit_order(symbol=randomright,qty=5,side="buy",type="market",time_in_force="day")
                        messagebox.askokcancel(randomright)
                         
          
                # Display detected face
                cv.imshow("Live Face Detection", frame)
                
            
                # condition to break out of while loop
                if cv.waitKey(20) == ord('x'):
                    break
           
            
        capture.release()
        cv.destroyAllWindows()
        #!(/face_detector)
