#import pywhatkit as kit
import pyttsx3
import os
import pyaudio
import speech_recognition
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import webbrowser
#from  PyQt5.uic import loadUiType
from agui import Ui_mainWindow
import sys
en=pyttsx3.init()
rate=en.getProperty("rate")
en.setProperty("rate",125)
voices=en.getProperty("voices")
en.setProperty("voice",voices[1].id)
password="hello"
def sp(audio):
    en.say(audio)
    en.runAndWait()
class Mainthread(QThread):
    def __init__(self):
        super(Mainthread, self).__init__()
    def run(self):
        sp("Hello sir,how are you feeling?")
        self.taskexecute()
    def takeaudio(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("listening.....")
            r.pause_threshold = 2.3
            audio = r.listen(source)
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print("user said:", query)
        except Exception as e:
            print(e)
            print("say something")
            return "none"
        return query
    def taskexecute(self):
        while True:
            self.query=self.takeaudio().lower()
            if  "good" in self.query:
                sp("That's great")
                sp("Have a great day ahead")
                continue
            elif "not fine" in self.query:
                sp("what is troubling you")
                resp=self.takeaudio().lower()
                if "fever" in resp:
                    sp("Can you please state any other symptoms")
                    qf3=self.takeaudio().lower()
                    print(qf3,end="")
                    print(("stomach ache" or "headache" or "constipation" or "cough" or "loss of appetite") in qf3)
                    if ("stomach ache" in qf3 or "headache"in qf3 or "constipation"in qf3 or "cough"in qf3 or "loss of appetite"in qf3):
                          sp("do you have headache or constipation or cough or loss of appetite" )
                          qf2=self.takeaudio().lower()
                          if "yes" in qf2:
                              sp("i think you may have typhoid ,consult your doctor")
                              os.startfile("F:\TEXTBOOKS\LDCO\\maxresdefault.jpg")
                              sp("your prescribed medication is as follows: Amikacin injection ,azithromycin tablet and ceftriaxone injection")
                              os.system("taskkill /IM Microsoft.Photos.exe /F")
                              sp("take care")
                          else:
                              sp("I thik you have seasonal influenza")
                    elif "nausea"in qf3 or "vommiting"in qf3 or "fatigue" in qf3:
                        sp("Do you have rapid breathing and heartrate  along with cough")
                        qf2=self.takeaudio().lower()
                        if "yes" in qf2:
                            sp("i think you may have Malaria ,consult your doctor")
                            os.startfile("F:\malaria.jpeg.jpeg")
                            sp("your prescribed medication is as follows: tablet artesunate plus tablet pcm plus tablet pan 40/emset and Tab primaquine")
                            os.system("taskkill /IM Microsoft.Photos.exe /F")
                            sp("take care")
                        else:
                            sp("I thik you have seasonal influenza")
                elif "loose or thin stools" in resp or "watery stool" in resp or "abdominal pain" in resp or "nausea" in resp or "loose motion"in resp:
                    sp("Do you feel bloating in belly region")
                    qd1=self.takeaudio().lower()
                    if "yes" in qd1:
                        sp("i think you may have diarrheoa ,consult your doctor")
                        os.startfile("F:\diaarheoa.jpeg")
                        sp("your prescribed medication is as follows:tablet lomotil + nutrolin B + Tab metronidazole")
                        os.system("taskkill /IM Microsoft.Photos.exe /F")
                        sp("take care")
                    else:
                        sp("You may have normal acidity avoid eating grasy food")
                        sp("for now you may take home remedies like cold milk or lemon juice")
            sp("Do you want to connect to our hospitals")
            qm1=self.takeaudio().lower()
            if "yes" in qm1:
                sp("which hospital do you want to connect Hospital A or Hospital B or Hospital C")
                q=self.takeaudio().lower()
                sp("please fill the form to which you are redirected")
                if "a" in q:
                  webbrowser.open("https://forms.gle/74rxwBuXQ1NDmCMv9")
                  continue
                elif "b" in q:
                    webbrowser.open("https://forms.gle/znrUCPem7847ucqU8")
                    continue
                elif "c" in q:
                    webbrowser.open("https://forms.gle/Y6KgZ8tGgcsZmVnz7")
                    continue














startexecution=Mainthread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)



    def startTask(self):
         self.ui.movie=QtGui.QMovie("giphy.gif")
         self.ui.label.setMovie(self.ui.movie)
         self.ui.movie.start()

         self.ui.movie.start()
         self.ui.movie = QtGui.QMovie("T8bahf.gif")
         self.ui.label_3.setMovie(self.ui.movie)
         self.ui.movie.start()

         startexecution.start()

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())

