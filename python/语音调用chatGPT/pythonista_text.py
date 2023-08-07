import json

import speech, sound, time

translator=Translator()
rec=sound.Recorder("audio.m4a")
rec.record()
time.sleep(5)
rec.stop()
result=speech.recognize("audio.m4a","zh-cn")
print(result[0] [0])

trans_text=translator.translate(result[0] [0],dest="en")
print(trans_text.text)
speech.say(trans_text.text,'en-UK')
