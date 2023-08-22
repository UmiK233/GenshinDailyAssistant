import os
from selenium import webdriver
from selenium.webdriver import EdgeOptions, ChromeOptions
from time import sleep
import requests
import hashlib
import math
import time
import random


def get_message(user, pw, uid):
    user = user
    pw = pw
    uid = uid
    try:
        options = EdgeOptions()
        options.add_argument("disable-blink-features=AutomationControlled")
        driver = webdriver.Edge(options=options)
    except:
        try:
            options = ChromeOptions()
            options.add_argument("disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(options=options)
        except:
            print("请安装Chrome浏览器或Edge浏览器")
    driver.get('https://user.mihoyo.com/#/login/password')
    username = driver.find_element("xpath", '//input[@type="text"]')
    sleep(1)
    username.send_keys(user)
    password = driver.find_element("xpath", '//input[@type="password"]')
    sleep(1)
    password.send_keys(pw)
    check = driver.find_element("xpath", '//div[@class="mhy-checkbox"]')
    check.click()
    login = driver.find_element('xpath', '//button[@type="submit"]')
    login.click()
    while True:
        try:
            driver.find_element("xpath", '//div[@class="operation"]')
            break
        except:
            pass
    Cookie = driver.execute_script('return document.cookie;')
    fp = open('./message.txt', 'w', encoding='utf8')
    fp.write(uid + '\n')
    fp.write(Cookie)
    driver.quit()
    fp.close()


def start():
    fp = open('./message.txt', 'r', encoding='utf8')
    role_id = str(fp.readline())
    role_id = role_id.replace('\n', '')
    Cookie = str(fp.readline())
    Cookie = Cookie.replace('\n', '')
    server = "cn_gf01"
    url = "https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/dailyNote?role_id=" + role_id + "&server=" + server
    timestamp = math.floor(time.time())
    timestamp = str(timestamp)
    randomInt = random.randint(100000, 200000)
    randomInt = str(randomInt)
    hashstring = "salt=" + "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs" + "&t=" + timestamp + "&r=" + randomInt + "&b=&q=" + "role_id=" + role_id + "&server=" + server
    keyhash = hashlib.md5(hashstring.encode(encoding='utf-8'))

    headers = {
        "Host": "api-takumi-record.mihoyo.com",
        "Connection": "keep-alive",
        'DS': timestamp + ',' + randomInt + ',' + keyhash.hexdigest(),
        'x-rpc-tool_verison': 'v1.6.0-bh3',
        'x-rpc-app_version': '2.55.1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 miHoYoBBS/2.55.1',
        'x-rpc-device_id': 'ce0c01d6-a45b-33e2-84c0-aadcafce50b5',
        'Accept': 'application/json,text/plain,*/*',
        'x-rpc-device_name': 'Xiaomi%20Mi%2010',
        'x-rpc-page': 'v1.6.0-bh3_#/ys/daily',
        'x-rpc-device_fp': '38d7ebbed00b8',
        'x-rpc-sys_version': '12',
        'x-rpc-client_type': '5',
        'Origin': 'https://webstatic.mihoyo.com',
        'X-Requested-With': 'com.mihoyo.hyperion',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://webstatic.mihoyo.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': Cookie
    }
    response = requests.get(url=url, headers=headers)
    obj = response.json()
    try:
        current_resin = obj["data"]["current_resin"]
        task = obj["data"]["finished_task_num"]
        is_extra_task_reward_received = obj["data"]["is_extra_task_reward_received"]
    except:
        return ["None", "None", "None"]
    return [task, current_resin, is_extra_task_reward_received]


if __name__ == "__main__":
    try:
        open('./message.txt', 'r', encoding='utf8')
    except:
        get_message()
    start()
