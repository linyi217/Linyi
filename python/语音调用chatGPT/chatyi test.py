import speech_recognition as sr  #语音转文字模块
#import pyaudio
import openai
import pyttsx3

while True:
    r=sr.Recognizer()   #创建麦克风对象
    engine = pyttsx3.init() #初始化麦克风

#通过麦克风输入音频进行语音识别
    with sr.Microphone(device_index=0) as source:
        engine.say("想问啥")
        engine.runAndWait()
        audio=r.listen(source)

        # r.energy_threshold=300
        # r.pause_threshold=1

#语音识别
    try:
        text=r.recognize_google(audio,language='zh-CN')
#   print('你说的是:{}'.format(text))

    except:
        engine.say("听不懂")
        engine.runAndWait()

#调用音频文件进行语音识别
# with sr.AudioFile("E:\Git\python3\语音调用chatGPT\harvard.wav") as source:
#     audio=r.record(source)
# output=r.recognize_google(audio,language='zh-cn')
#print(output)

#调用chatGPT
        question=(text)
        openai.api_key='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'    
        response=openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"Question: {question}\nAnswer:"),
            temperature=0.9,
            max_tokens=4000,
            n=1,
            stop=None,
        )

    answer=response.choices[0].text.strip()

#chatGPT返回的文字转换为语音输出
    engine.say(answer)
    engine.runAndWait()

