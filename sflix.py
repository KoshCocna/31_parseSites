import requests, csv
from bs4 import BeautifulSoup

URL = "https://sflix.to/home"

soup_raw = requests.get(url=URL).text
soup = BeautifulSoup(soup_raw, "html.parser")
soup_1 = soup.find(id="trending-movies", class_="tab-pane active")
soup_2 = soup.find(class_="block_area block_area_home section-id-02")

trending = soup_1.find_all(class_="flw-item")
latest = soup_2.find_all(class_="flw-item")

data = trending + latest

with open("sflix.csv", "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "year", "rating", "quality"])
    for _ in data:
        film_info = _.findAllNext(name="span", class_="fdi-item")
        film_rating = film_info[0].text
        film_quality = film_info[1].text
        film_year = film_info[2].text
        film_name = _.find(name="h3", class_="film-name").text.rstrip('\n')
        writer.writerow([film_name, film_year, film_rating, film_quality])

    # for _ in latest:
    #     film_info = _.findAllNext(name="span", class_="fdi-item")
    #     film_rating = film_info[0].text
    #     film_quality = film_info[1].text
    #     film_year = film_info[2].text
    #     film_name = _.find(name="h3", class_="film-name").text
    #     writer.writerow([film_name, film_year, film_rating, film_quality])
