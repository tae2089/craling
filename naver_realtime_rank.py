import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def main():
    chrome_driver = '/Users/imtaebin/Documents/data_project/chromedriver'
    driver = webdriver.Chrome(chrome_driver)
    url = "https://www.naver.com/srchrank?frm=main&ag=all&gr=1&ma=0&si=0&en=-2&sp=0"
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'charset': 'utf-8',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cookie': 'NNB=FR7MCJNU2UNF4; ASID=01f8764a0000016f99eee0ae00000057; _ga_7VKFYR6RV1=GS1.1.1579138589.1.1.1579139294.0; NM_RTK_VIEW_GUIDE=1; NRTK=ag#all_gr#1_ma#0_si#0_en#-2_sp#0; _ga_4BKHBFKFK0=GS1.1.1580794744.1.1.1580794760.44; tae2089_word_speech_bubble_20140109=true; _ga=GA1.2.771222502.1578979351; nx_ssl=2; PM_CK_loc=0e45d7615363278bec6d127bdc948ab415e0becc4fb797cebe447e2746ad38b9; PM_CK_sclFixed=1; nid_inf=-1221046527; NID_AUT=A0En7LYmVq5B/RAr6IZH8QTda/QgWSlD0hx6bdjFbJJ2pZpYSOnZzLYpu5BYilzS; NID_JKL=x2xaexRRK5UAy2gihu+0LZ2FVZhA+iAMGohYPRcu9fs=; page_uid=UFEeVdprvTosskHlmqNssssstUZ-415891; NID_SES=AAABmtr9SuKUFFzZArV1hMecWkc+021q4yb2M5LF7Sw1sD8FJe7V5B5xVfxqwQfSAm/Iyoz4OWafFvVpFWnxrgTN4BykzE20Aq47gGe5lJER3Wr1Do2UyP0AqtPmzJTS7pDDjEAgCtMw/LZCBr97vOfsQS1Yp3Jq398mFzDo/9jIJmhVJjYaY9eIlf9zDz523quPGK2wsKx4EyKTp/uBY1xqjRvF4k0CDPZpyUa1wS5klx7pT1CG2vjl1Tu0WPpBMjs/hTzRRoxS76ib6AQ75PjfBt+y31J1n066H1KDi8JsOBWYjO9xS7OdGJDfiSLClCo0FGbDF10IML/eXpNMizkkPxH7vOOGhrlOIHJIulcsz/Y4xspx3B+4/Ync9/FmNd6E5/3q3qqQVJOoRcKyy0Anhzp6dXubSlcy7o8eKRr4Qh3CCOE/9765vtaOz2bc+eDbPt7QgskHny8KtjVyYXy+agof3yjjpDvRLPtNDHMqeZKKHd1QU9clqFCpMU+KLRjY6LFkBO/WXJlCBUxRarLOI603ZnaUPyUnfCT3KOB27Q20',
        'referer': 'https://www.naver.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    html = requests.get(url, headers=headers)
    data = html.json()
    data1 = data['data']
    for i in range(len(data1)):
        a = data1[i]
        print(a['rank'], ":", a['keyword'])

        
if __name__ == "__main__":
    main()
