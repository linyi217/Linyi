#-*-coding:utf-8-*-
"""
Jax AI Voice, 语音互动
"""
import time
import speech_recognition as sr  # 语音转文字模块
import openai
import pyttsx3  # 文字转语音


def jax_ai():
    """
    Jax AI Voice
    Returns:

    """
    # 定义初始值
    first_time = True
    while True:
        r = sr.Recognizer()  # 创建麦克风对象
        engine = pyttsx3.init()  # 初始化麦克风
        # 设置台湾女生普通话发音
        engine.setProperty(
            'voice', "com.apple.speech.synthesis.voice.mei-jia")
        # 通过麦克风输入音频进行语音识别
        with sr.Microphone(device_index=0) as source:
            time.sleep(2)
            # 如果是第一次询问
            if first_time:
                # 文字转语音
                engine.say("你好主人")
                # 取消首次标记，下次进入非第一次询问的逻辑
                first_time = False
            # 非第一次询问
            else:
                # 文字转语音
                engine.say("还有什么想问的吗")
            # 播放语音
            engine.runAndWait()
            # 监听麦克风接收到音频
            audio = r.listen(source)
        try:
            # 识别麦克风接收到的音频，转为文字
            text = r.recognize_google(audio, language="zh-CN", show_all=False)  # 需要开外网，调用google语音识别
            print('你说的是:{}'.format(text))  # 查看转换的文字是否准确
            # 如果文字是以结束或没有开头，
            if text.startswith('结束') or text.startswith('没有'):
                engine.say("主人再见")
                print('主人再见')
                engine.runAndWait()
                # 中断循环
                break
            openai.api_key = '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'
            # 请求chatGPT接口
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=(f"Question: {text}\nAnswer:"),
                temperature=0.9,
                max_tokens=4000,
                n=1,
                stop=None,
            )
            # 获取答案
            answer = response.choices[0].text.strip()
            print('答案：' + answer)
            # chatGPT返回的文字转换为语音
            engine.say(answer)
            # 播放语音
            engine.runAndWait()
        except KeyboardInterrupt:
            print('再见')
        except sr.UnknownValueError:
            print('没有收到任何回应')


if __name__ == '__main__':
    jax_ai()