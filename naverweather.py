from ctypes import cast
from sre_constants import MAX_REPEAT
import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hykvudp0Yidssn0b4kwssssstx8-238372"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    cast = soup.find("p", attrs={"class":"summary"}).get_text()

    # 현재온도, 최고온도, 최저온도 불러오기
    curr_temp = soup.find("div", attrs={"class": "temperature_text"}).get_text().replace("도씨", "") # 현재온도
    min_temp = soup.find("span", attrs={"class": "lowest"}).get_text() # 최저온도
    max_temp = soup.find("span", attrs={"class": "highest"}).get_text() # 최고온도

    # 오전/오후 강수 확률
    rain_rate = soup.find("div", attrs={"class":"cell_weather"}).get_text().strip() # 오전, 오후 강수확률

    # 출력
    print(cast)
    print("{} ( {} / {})".format(curr_temp,min_temp,max_temp))
    print("{}".format(rain_rate))

if __name__ == "__main__" :
    scrape_weather() # 오늘의 날씨 정보 가져오기