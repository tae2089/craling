from urllib.request import urlopen 
from urllib.parse import quote_plus 
from bs4 import BeautifulSoup 
from selenium import webdriver 
import time 
import requests 
import shutil 

def main():
    baseUrl = 'https://www.instagram.com/explore/tags/' 
    plusUrl = input('검색할 태그를 입력하세요 : ') 
    url = baseUrl + quote_plus(plusUrl) 
    chrome_driver = '/Users/imtaebin/Documents/Data_stduy/chromedriver'
    driver = webdriver.Chrome(chrome_driver) 
    driver.get(url) 
    time.sleep(3) 
    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')
    imglist = [] 
    for i in range(0, 5): 
        insta = soup.select('.v1Nh3.kIKUG._bz0w') 
        for i in insta: 
            imgUrl = 'https://www.instagram.com' + i.a['href']
            imglist.append(imgUrl) 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        time.sleep(2)
    




if __name__ == "__main__":
    main()
