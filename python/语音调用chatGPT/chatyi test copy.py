import speech_recognition as sr  #语音转文字模块
#import pyaudio
import openai
import pyttsx3  #文字转语音


while True:
    r=sr.Recognizer()   #创建麦克风对象
    engine = pyttsx3.init() #初始化麦克风

#通过麦克风输入音频进行语音识别
    with sr.Microphone(device_index=0) as source:
        engine.say("想问啥")   #听到“想问啥”，开始说话
        engine.runAndWait()
        audio=r.listen(source)
        
    try:
        text=r.recognize_google(audio,language="zh-CN")   #需要开外网，调用google语音识别
        print('你说的是:{}'.format(text))   #查看转换的文字是否准确

    except:
        print('正在听')
        #engine.say("听不懂")
        #engine.runAndWait()

#调用chatGPT
        if "你好" in text:
            question=(text.split("你好")[1])
            print('筛选后是:{}'.format(question))   #筛选后的文字是否准确
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
            print(answer)   #查看chatGPT返回内容是否准确

#chatGPT返回的文字转换为语音输出
            engine.say(answer)
            engine.runAndWait()

            engine.say("还有什么想问的吗")
            engine.runAndWait()
