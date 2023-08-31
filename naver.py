from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def get_url(field: str):
    url = {
        "1": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=731", "mobile"],
        "2": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=226", "internet"],
        "3": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=227", "communication"],
        "4": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230", "IT"],
        "5": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=732", "security"],
        "6": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=283", "computer"],
        "7": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=229", "game"],
        "8": ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=228", "science"]
    }
    return url.get(field, ["https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=731", "mobile"])


def parsing(source_url):
    with open(f"{source_url[1]}_news.csv", "w", encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "field", "title"])
        driver.get(source_url[0])
        data = driver.find_elements(By.CSS_SELECTOR, ".newsflash_body a")
        id = 0
        for _ in data:
            try:
                title = _.text
                if title != '':
                    id += 1
                    writer.writerow([id, source_url[1], title])
            except:
                pass


if __name__ == "__main__":
    wanna_continue = True
    while wanna_continue:
        driver = webdriver.Chrome()
        tema = input(
            "select the id according to the field\n<If you want to quit, then press q>\n모바일-1, 인터넷-2, 통신-3, 일반-4, 보안-5, 컴퓨터-6, 게임-7, 과학-8: ").lower()
        if tema == "q":
            wanna_continue = False
        else:
            URL = get_url(tema)
            parsing(URL)
        driver.quit()
