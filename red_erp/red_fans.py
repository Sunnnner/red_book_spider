import time

import pandas as pd
import requests
from openpyxl import Workbook

from red_erp.whosecard_open_platform import WhosecardXhsSpider

xhs = WhosecardXhsSpider()
wb = Workbook()
ws = wb.active
ws.append([
    "用户名",
    "粉丝数"
])


def get_fans(u_id):
    try:
        result = xhs.get_user_info(u_id)
        user_info = result['result']['data']
        user_name = user_info['nickname']
        fans = user_info['fans']
        print([user_name, fans])
        ws.append([user_name, fans])
        wb.save(r"D:\red_book\red_book_51wom\red_book_9月\red_book_09_28\fans.xlsx")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    df = pd.read_excel(r"D:\red_book\red_book_51wom\red_book_9月\red_book_09_28\red_urls.xlsx")
    urls = df['主页链接']
    for url in urls:
        if 'apptime' in url:
            u_id = url.split("/")[-1].split("?")[0]
        else:
            u_id = url.split("/")[-1]
        get_fans(u_id)
        # time.sleep(5)