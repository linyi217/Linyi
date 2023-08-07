import openai

question=input("想问啥?")

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
print("答:{}".format(answer))

#if answer==str():
#    question



