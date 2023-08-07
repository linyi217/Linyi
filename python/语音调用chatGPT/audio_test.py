#import pyaudio
import pyttsx3
import speech_recognition as sr
#import pyaudio

engine = pyttsx3.init()
q=engine.say("I will speak this text")
engine.runAndWait()

#创建麦克风对象
r=sr.Recognizer()

#使用麦克风对象进行语音识别
<<<<<<< HEAD
with sr.Microphone(device_index=0) as source:
   print('请说话:')
   audio=r.listen(source)

   r.energy_threshold=300
   r.pause_threshold=1

#语音识别
try:
  text=r.recognize_google(audio,language='zh-CN')
  print('你说的是:{}'.format(text))
except:
  print('请说中文')


#识别音频文件
# with sr.AudioFile("E:\Git\python3\语音调用chatGPT\harvard.wav") as source:
#     audio=r.record(source)
# output=r.recognize_google(audio,language='zh-cn')
# print(output)
=======
#with sr.Microphone(device_index=0) as source:
#    print('请说话:')
#    audio=r.listen(source)

#语音识别
#try:
#    text=r.recognize_google(audio,language='zh-CN')
#    print('你说的是:{}'.format(text))
#except:
#    print('请说中文')



with sr(q) as source:
    audio=r.record(source)
output=r.recognize_google(audio,language='zh-cn')
print(output)
>>>>>>> 10e7b16aacfb6c7a016bd6ef84f69d11dfcc0aef

