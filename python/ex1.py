import os

import requests
from bs4 import BeautifulSoup

# 确定要保存照片的文件夹名称
directory_name = 'cat_photos'

# 确保文件夹存在
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

# 发送HTTP请求并获取响应
url = 'http://www.cutestpaw.com/tag/cats/'
response = requests.get(url)
html = response.text

# 解析HTML并查找猫咪照片
soup = BeautifulSoup(html, 'html.parser')
photo_list = soup.find_all('img', {'class': 'photo-img'})

# 下载每张照片并保存到文件夹中
for i, photo in enumerate(photo_list):
    photo_url = photo['src']
    response = requests.get(photo_url)
    with open(os.path.join(directory_name, f"cat_{i}.jpg"), 'wb') as f:
        f.write(response.content)
    print(f"Downloaded cat photo {i+1} out of {len(photo_list)}")
