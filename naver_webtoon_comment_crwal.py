import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import time
import re
import os
import json
import sys
import traceback
import threading


def make_list(soup, tag_url):
    tag_list = soup.select(tag_url)
    #문자열화
    tag_list = list(map(lambda x: str(x), tag_list))
    #태그 제거
    tag_list = list(map(lambda x: re.sub(
        '<.+?>', '', x, 0, re.I | re.S), tag_list))
    #앞뒤 공백 제거
    tag_list = list(map(lambda x: x.strip(), tag_list))
    return tag_list
def sub_comment_code(soup,tag_url):
    tag_list = soup.select(tag_url)
    tag_list = list(map(lambda x: x['class'][1].split("_")[4], tag_list))
    return tag_list

def browser_start():
    #드라이버 넣기
    chrome_driver = '/Users/imtaebin/Documents/data_project/chromedriver'
    #드라이버 주소
    browser = webdriver.Chrome(chrome_driver)
    #웹 주소
    url = "https://comic.naver.com/comment/comment.nhn?titleId=641253&no=306"
    browser.get(url)
    #전체 댓글 모드
    browser.find_element_by_partial_link_text('전체댓글').click()
    time.sleep(0.4)
    #클린봇 설정 들어가기
    browser.find_element_by_class_name('u_cbox_cleanbot_setbutton').click()
    time.sleep(0.4)
    #클린봇 클릭
    browser.find_element_by_class_name(
        'u_cbox_layer_cleanbot_checkbox').click()
    time.sleep(0.4)
    #클린봇 나가기
    browser.find_element_by_class_name(
        'u_cbox_layer_cleanbot_extrabutton').click()
    time.sleep(0.4)

    return browser


def page_crawling(soup, result):
    #코멘트 고유 식별 번호
    comment_code = sub_comment_code(
        soup, "#cbox_module_wai_u_cbox_content_wrap_tabpanel > ul > li")
    #닉네임
    nickname = make_list(
        soup, ".u_cbox_list li div.u_cbox_comment_box div.u_cbox_area span.u_cbox_nick_area")
    # 마스킹된 아이디
    mask_id = make_list(
        soup, ".u_cbox_list li div.u_cbox_comment_box div.u_cbox_area span.u_cbox_id_area")
    #댓글 작성시간
    comment_date = make_list(
        soup, ".u_cbox_list li div.u_cbox_comment_box div.u_cbox_area span.u_cbox_date")
    #댓글 내용
    comment_contents = make_list(
        soup, ".u_cbox_list li div.u_cbox_comment_box div.u_cbox_area span.u_cbox_contents")
    #종아요 갯수
    recomm = make_list(
        soup, ".u_cbox_list li div.u_cbox_comment_box div.u_cbox_area em.u_cbox_cnt_recomm")
    #싫어요 갯수
    unrecomm = make_list(
        soup, ".u_cbox_list li div.u_cbox_comment_box div.u_cbox_area em.u_cbox_cnt_unrecomm")
    #댓글 클린 여부
    is_clean = False

    for i in range(len(nickname)):
        a = {
            "comment_code":comment_code[i],
            "nickname": nickname[i],
            "mask_id": mask_id[i],
            "comment_date": comment_date[i],
            "comment_contents": comment_contents[i],
            "recomm": recomm[i],
            "unrecomm": unrecomm[i],
            "is_clean": is_clean
        }
        result.append(a)
    #print(result)
    return result


def click_num_page(num, result, browser):
    while True:
        try:
            browser.find_elements_by_class_name('u_cbox_num_page')[num].click()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_num_page')))
            break
        except:
            print("do it again")
    time.sleep(0.4)
    html = browser.page_source
    time.sleep(0.4)
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(0.4)
    result = page_crawling(soup, result)
    time.sleep(0.4)
    return result, browser, num+1


def click_next_page(result, browser):
    firstElementXPath = '//*[@id="cbox_module"]/div/div[6]/ul/li[1]'
    while True:
        try:
            browser.find_elements_by_class_name('u_cbox_cnt_page')[2].click()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, firstElementXPath)))
            break
        except:
            print("do it again")
    time.sleep(0.4)
    html = browser.page_source
    time.sleep(0.4)
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(0.4)
    result = page_crawling(soup, result)
    time.sleep(0.4)
    return result, browser

def total_page_cnt(browser):
    html = browser.page_source
    time.sleep(0.4)
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(0.4)
    a = make_list(soup, "#cbox_module > div > div.u_cbox_head > span")
    a = list(map(lambda x: x.replace(",", ""), a))
    a = int(a[0])
    page_cnt = 0
    if a % 15 == 0:
        page_cnt = a // 15
    else:
        page_cnt = (a // 15) + 1
    print("total_page_cnt:", page_cnt)
    return page_cnt


def main():
    result = []
    #webdreiver 설정
    while True:
        try:
            browser = browser_start()
            break
        except:
            print("do it again")
    num = 0
    start = time.time()  # 시작 시간 저장
    page_cnt = total_page_cnt(browser)
    for i in range(0, page_cnt):
        if num == 10:
            num = 1
            result, browser = click_next_page(result, browser)
            print(i)
        else:
            result, browser, num = click_num_page(num, result, browser)
            print(i)

    print("time :", time.time() - start)
    df = pd.DataFrame(result)
    df.to_excel("test.xlsx")
    browser.quit()


if __name__ == "__main__":
    main()
