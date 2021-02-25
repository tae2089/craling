import requests
from bs4 import BeautifulSoup


def main():
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    resp = requests.get(url)
    result = BeautifulSoup(resp.text)
    result.select("div.tit3 a")
    movie_ran_list = []
    for i,p in enumerate(result.select("div.tit3 a")):
        print("{}위:{}".format(i+1,p.get_text()))
    #print(movie_ran_list)

if __name__ == "__main__":
    main()
