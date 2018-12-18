# -*- coding: utf-8 -*-
# @Time    : 18-12-16 下午5:12
# @Author  : liu
# @Project : ProxyPool
# @File    : get_proxy.py
# @Software: PyCharm
import requests

PROXY_POOL_URL = 'http://localhost:5555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


def main():
    proxy = get_proxy()
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


if __name__ == '__main__':
    main()
