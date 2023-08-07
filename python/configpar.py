import configparser

# 创建一个 ConfigParser 对象
config = configparser.ConfigParser()

# 在配置文件中添加一个节
config.add_section('EMAIL')
config.add_section('MYSQL')

# 在配置文件中添加一个配置项
config.set('MYSQL', 'host', '121.43.55.85')
config.set('MYSQL', 'port', '3306')
config.set('MYSQL', 'user', 'lwz')
config.set('MYSQL', 'password', 'QQqq11!!')

# 设置 EMAIL 节中的选项值
config.set('EMAIL', 'SERVER', 'smtp.gmail.com')
config.set('EMAIL', 'PORT', '587')
config.set('EMAIL', 'USERNAME', 'wzlin217@gmail.com')
config.set('EMAIL', 'PASSWORD', 'gswnbzjm217.')

# 将配置写入文件
with open('config.ini', 'w') as f:
    config.write(f)
