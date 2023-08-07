import openai
import sys

def chat_map(ask_string):
    """

    Returns:

    """
    openai.organization = "org-0FpS2QCVYNdQx91WASOjtF75"
    openai.api_key = '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'
    model_engine ="text-davinci-003"
    prompt = ask_string
    # print(openai.Model.list())
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

if __name__ == '__main__':
    try:
        ask_string = ' '.join(sys.argv[1:])
        message = chat_map(ask_string)
        print(message.strip())
    except IndexError:
        print("您有什么想问的?请在脚本后输入")
