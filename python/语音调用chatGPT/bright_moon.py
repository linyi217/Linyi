# -*-coding:utf-8-*-
"""
Jax AI Voice - Bright Moon, 智能语音互动
"""
import speech_recognition as sr  # 语音转文字模块
import openai
import pyttsx3  # 文字转语音
import time


class BrightMoon(object):
    """
    Bright Moon
    """
    openai.api_key = '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'
    my_name = u'明月'
    master_name = u'主人'
    end_words = [u'再见', u'结束', u'拜拜']
    # 定义保持持续沟通的信号字
    keep_talk_sign = '开启持续对话'
    disable_keep_talk_sign = '关闭持续对话'
    bright_moon_response_word = '我在'

    def __init__(self):
        """
        类初始化
        """
        self.engine = pyttsx3.init()  # 初始化
        # 设置台湾女生普通话发音
        self.engine.setProperty(
            'voice', "com.apple.speech.synthesis.voice.mei-jia")
        # 文字转语音
        self.engine.say("你好{0},{1}已进入监听状态".format(self.master_name, self.my_name))
        # 取消首次标记，下次进入非第一次询问的逻辑
        self.engine.runAndWait()
        self.latest_answer = str()

    def bright_moon(self):
        """
        Jax AI Voice - Bright Moon
        Returns:

        """
        # 定义初始值
        ask_gpt = True
        keep_talk = False
        first_time = True
        r = sr.Recognizer()  # 创建麦克风对象
        num = 0
        mic = sr.Microphone()
        with mic as source:
            # 创建一个无限循环
            while True:
                num += 1
                print('开始第{}次循环识别'.format(num))
                # 监听麦克风接收到音频
                print('开始监听')
                start_listen_time = time.time()
                # 可添加snowboy_configuration参数，指定唤醒词
                try:
                    audio = r.listen(source, timeout=10, phrase_time_limit=10)
                except sr.WaitTimeoutError:
                    print('检测到超时')
                    continue
                # 识别麦克风接收到的音频，转为文字
                print('已监听{}秒开始获取语音内容'.format(int(time.time() - start_listen_time)))
                question = r.recognize_google(audio, language="zh-CN", show_all=True)  # 需要开外网，调用google语音识别
                print('已获取到语音内容')
                # 基于收集到的语音内容判断是否继续往下执行。
                if question:
                    question = question['alternative'][0]['transcript']
                    print('你说的是: {}'.format(question))  # 查看转换的文字是否准确
                else:
                    print('空内容{}'.format(question))
                    continue
                # 判断是否要询问gpt
                if ask_gpt or keep_talk or first_time:
                    answer = self.ask_gpt_question(question)
                    # chatGPT返回的文字转换为语音
                    self.engine.say(answer)
                    # 播放语音
                    self.engine.runAndWait()
                    ask_gpt = False
                    first_time = False
                # 如果文字是以结束或没有开头，
                elif self.verify_end(question):
                    self.engine.say("{}再见".format(self.master_name))
                    print('{}再见'.format(self.master_name))
                    self.engine.runAndWait()
                    # 中断循环
                    break
                elif question.__contains__(self.keep_talk_sign):
                    keep_talk = True
                    self.engine.say("收到，持续对话已开启。")
                    self.engine.runAndWait()
                elif question.__contains__(self.disable_keep_talk_sign):
                    keep_talk = False
                    self.engine.say("收到，持续对话已关闭。")
                    self.engine.runAndWait()
                elif question.__contains__(self.my_name):
                    self.engine.say(self.bright_moon_response_word)
                    self.engine.runAndWait()
                    # ask_gpt 设置为True，表示下次可以去查询gpt
                    ask_gpt = True

    def ask_gpt_question(self, question):
        """
        Ask GPT question
        Args:
            question: Question

        Returns:

        """
        if question.startswith(self.my_name):
            question = question.lstrip(self.my_name)
        # 定义openai允许的最大长度
        max_length = 4097
        # 如果本次询问加上上次的答案会超过最大长度，则将上次的答案置空
        if len(question) + len(self.latest_answer) > max_length:
            self.latest_answer = str()
        # 请求openai接口, 获取答案
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Question: {question}\nAnswer:{self.latest_answer}",
            temperature=0.9,
            max_tokens=4000,
            n=1,
            stop=None,
        )
        # 获取答案内容
        self.latest_answer = response.choices[0].text.strip()
        print('答案：' + self.latest_answer)
        return self.latest_answer

    def verify_end(self, question):
        """
        核实是否需要结束
        Args:
            question: Question

        Returns:

        """
        for end_word in self.end_words:
            if question.startswith(end_word):
                return True
        return False

    def run(self):
        """
        Bright Moon Main Function
        Returns:

        """
        try:
            self.bright_moon()
        except KeyboardInterrupt:
            print('再见')
        except AttributeError:
            print('麦克风可能未正常接入，建议使用耳机')


if __name__ == '__main__':
    # BrightMoon().run()
    bm = BrightMoon
    bm.my_name = '明月'
    bm().run()
