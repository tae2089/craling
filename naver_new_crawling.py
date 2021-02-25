import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import csv
# 반복1: 기사번호를 변경시키면서 데이터 수집을 반복하기
# 1 ~ 100까지 10단위로 반복(1, 11, ..., 91)
def main():
    data_list = [["주소","제목","보도국"]]
    ds = datetime.now() - relativedelta(months=1)
    de = datetime.today().strftime("%Y.%m.%d")
    cnt = 0
    url = "https://search.naver.com/search.naver?where=news&query={}&ds={}&de={}&start=".format('\"사회공헌\"',ds,de)
    print(url)
    for n in range(1, 100, 10):
        raw = requests.get(url+str(n), headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(raw.text, "html.parser")

        articles = html.select("ul.list_news > li")

    # 반복2: 기사에 대해서 반복하면 세부 정보 수집하기
    # 리스트를 사용한 반복문으로 모든 기사에 대해서 제목/언론사 출력
        for i,ar in enumerate(articles):
            cnt+=1
            href = ar.select_one(
                "div.news_wrap.api_ani_send > div > a")["href"]
            title = ar.select_one(
                "div.news_wrap.api_ani_send > div > a")["title"]
            source = ar.select_one(
                "div.news_wrap.api_ani_send > div > div.news_info > div > a.info.press").text
            data = [href,title,source]
            data_list.append(data)
    with open('/Users/imtaebin/Downloads/sample_test.csv', 'w', newline='',encoding="euc-kr") as f:
        makewrite = csv.writer(f) 
        for value in data_list: 
            try:
                makewrite.writerow(value)
            except:
                pass
            

if __name__ == "__main__":
    main()
