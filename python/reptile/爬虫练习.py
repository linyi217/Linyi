import requests

urls = ['http://www.baidu.com/search?q=斗破苍穹',
        'http://www.baidu.com/search?q=熊猫']

for url in urls:
    r = requests.get(url)
    print(r.text)

    # do something with the response here