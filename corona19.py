import json
import xmljson
import requests
import xmltodict
from datetime import datetime,timedelta



def main():
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=QL9to6a%2FKkN03fsBGPP7aXvXskWMawBGUGcUwTJIjKRTcmElvHVZQKZ6HD1htmJ5gvUtPf6ivE5YW18fJcVGsQ%3D%3D&pageNo=1&numOfRows=1000&startCreateDt={}&endCreateDt={}'

    today= datetime.today().strftime('%Y%m%d')
    now = datetime.now()
    now_week_ago = now - timedelta(days=7)
    now_week_ago = now_week_ago.strftime("%Y%m%d")

    url = url.format(now_week_ago,today)
    resp = requests.get(url)
    xmlString = resp.text
    corona_json = json.dumps(xmltodict.parse(xmlString), indent=4)
    print(corona_json)

if __name__ == "__main__":
    main()
