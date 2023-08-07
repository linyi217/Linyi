import speech_recognition as sr  #语音转文字模块
#import pyaudio
import openai
import pyttsx3


#创建麦克风对象
r=sr.Recognizer()


#通过麦克风输入音频进行语音识别
#with sr.Microphone() as source:
#    print('请说话:')
#    audio=r.listen(source)

#语音识别
#try:
#    text=r.recognize_google(audio,language='zh-CN')
#    print('你说的是:{}'.format(text))
#except:
#    print('请说中文')

while True:

#调用音频文件进行语音识别
    with sr.AudioFile("E:\Git\python3\语音调用chatGPT\harvard.wav") as source:
        audio=r.record(source)
    output=r.recognize_google(audio,language='zh-cn')
#print(output)

    if output=="没有了":
        break           #当语音出现"没有了"，结束循环。

#调用chatGPT
    question=(output)
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
    #print(answer)


#chatGPT返回的文字转换为语音输出
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()

