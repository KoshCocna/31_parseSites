import requests, csv
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
}


def parsing(url):
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url).text

        soup = BeautifulSoup(r, 'lxml')
        useful_info = soup.find_all(class_="vacancy-serp-item__layout")
        file = open('hh.csv', 'w', encoding='utf8', newline='')
        writer = csv.writer(file)
        writer.writerow(["vacancy", "salary", "company", "city"])
        for _ in useful_info:
            vacancy = _.find(name="a", class_="serp-item__title").getText()
            try:
                salary = _.find(name="span", class_="bloko-header-section-2").text
            except:
                salary = "ЗП не  указана"
            try:
                company = _.find(name="a", class_="bloko-link bloko-link_kind-tertiary").text
            except:
                company = "не указана"
            try:
                city = _.findAllNext(class_="bloko-text")[1].text
            except:
                city = "не указана"
            writer.writerow([vacancy, salary, company, city])

        file.close()

def get_url(field: str):
    fore_url = "https://vladivostok.hh.ru/vacancies/programmist_"
    back_url = "?hhtmFromLabel=rainbow_profession&hhtmFrom=main"
    url = {
        "1": fore_url+"python"+back_url,
        "2": fore_url+"android"+back_url,
        "3": fore_url+"ios"+back_url,
        "4": fore_url+"javascript"+back_url,
        "5": fore_url+"c_plus_plus"+back_url,
        "6": fore_url+"java"+back_url,
        "7": fore_url+"c_sharp"+back_url,
        "8": fore_url+"sql"+back_url
    }
    return url.get(field, "https://vladivostok.hh.ru/vacancies/programmist_python?hhtmFromLabel=rainbow_profession&hhtmFrom=main")


if __name__ == "__main__":
    tema = input("select the vacancy field\npython:1, android:2, iOS:3, JS:4, C++:5, JAVA:6, C#:7, SQL:8:  ")
    URL = get_url(tema)
    print(URL)
    parsing(URL)