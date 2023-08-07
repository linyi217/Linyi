<<<<<<< HEAD
import pyttsx3  #文字转语音
import speech_recognition as sr   #语音转文字

engine = pyttsx3.init()
q=engine.say("贾克斯")
engine.runAndWait()

r=sr.Recognizer()

with sr.AudioFile(q) as source:
    audio=r.record(source)
output=r.recognize_google(audio,language="zh-cn")
print(output)
=======
import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
>>>>>>> 10e7b16aacfb6c7a016bd6ef84f69d11dfcc0aef
