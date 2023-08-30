import requests
from bs4 import BeautifulSoup


def get_url(field: str):
    url = {
        "1": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=731",
        "2": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=226",
        "3": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=227",
        "4": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230",
        "5": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=732",
        "6": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=283",
        "7": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=229",
        "8": "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=228"
    }
    return url.get(field, "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=731")


def parsing(source_url):
    soup_raw = requests.get(url=source_url).text
    soup = BeautifulSoup(soup_raw, "html.parser")
    data = soup.find(name="ul", class_="type06_headline")
    # Couldn't parse
    print(data)


if __name__ == "__main__":
    tema = input("select the id according to the field\n모바일-1, 인터넷-2, 통신-3, 일반-4, 보안-5, 컴퓨터-6, 게임-7, 과학-8:  ")
    URL = get_url(tema)
    print(URL)
    parsing(URL)
