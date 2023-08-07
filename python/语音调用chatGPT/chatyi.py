
#import os
import time

import openai

#from dotenv import load_dotenv

#load_dotenv()

time.sleep(3)

<<<<<<< HEAD
openai.api_key='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'

question=("你好")
=======
question=input("想问啥?")
>>>>>>> e37d00d7036f143a2b259c2d5cbcdef804fe46fb
#context=""

response=openai.Completion.create(
    engine="text-davinci-002",
    prompt=(f"Question: {question}\nAnswer:"),
    temperature=0.9,
    max_tokens=4000,
    n=1,
    stop=None,
)

answer=response.choices[0].text.strip()
print(answer)
