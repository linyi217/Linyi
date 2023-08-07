#import configparser
import datetime
import smtplib
from email.mime.text import MIMEText

import pymysql

#config = configparser.ConfigParser()
#config.read(".config.ini")


# MySQL数据库配置信息
mysql_config = {
    'host': '116.62.213.248',
    'user': 'lwz',
    'password': 'QQqq11!!',
    'port': 3306,
#    'db': 'testdb'
}

mysql_config2 = {
    'host': '121.43.55.85',
    'user': 'lwz',
    'password': 'QQqq11!!',
    'port': 3306,
#    'db': 'testdb'
}

# 邮箱配置信息
mail_config = {
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 587,
    'user': 'wslinwanzhang@qq.com',
    'password': 'nrstwenaxvthcacf',
    'from_addr': 'wslinwanzhang@qq.com',
    'to_addr': 'wzlin217@gmail.com'
}

def check_mysql_slave_status():
    # 连接MySQL数据库
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor()

    conn = pymysql.connect(**mysql_config2)
    cursor = conn.cursor()

    # 查询主从同步状态信息
    cursor.execute("SHOW SLAVE STATUS")
    result = cursor.fetchone()

    # 判断主从同步是否正常
    if result is None:
        return "主从同步已断开！"

    slave_io_running = result[10]
    slave_sql_running = result[11]

    if slave_io_running != 'Yes' or slave_sql_running != 'Yes':
        return "主从同步已断开！"

    return "主从同步正常。"

def send_email(subject, message):
    # 创建邮件对象
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = mail_config['from_addr']
    msg['To'] = mail_config['to_addr']
    msg['Subject'] = subject

    # 连接SMTP服务器，发送邮件
    server = smtplib.SMTP(mail_config['smtp_server'], mail_config['smtp_port'])
    server.starttls()
    server.login(mail_config['user'], mail_config['password'])
    server.sendmail(mail_config['from_addr'], [mail_config['to_addr']], msg.as_string())
    server.quit()

if __name__ == '__main__':
    # 检查主从同步状态
    sync_status = check_mysql_slave_status()
    

    # 判断是否发送邮件提醒
    now = datetime.datetime.now()
    if sync_status == "主从同步正常。" or (now.hour == 10 and now.minute == 4):

        send_email("MySQL主从同步状态",sync_status,'以下为运营02具体信息:'+result)
