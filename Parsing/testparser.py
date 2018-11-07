import csv
import requests
from bs4 import BeautifulSoup  


def get_html(url):
    response = requests.get(url)
    return response.text

def get_tasks(soup):
    tasks = soup.find('div', id="projects-list")
    tasks = tasks.find_all('h2', class_="b-post__title b-post__title_inline ")
   
    for task in tasks:
        a = task.find('a', class_="b-post__link").get('href')
        link = "https://www.fl.ru" + a
        print(link)

def main():
    url = 'https://www.fl.ru/projects/'
    a = 1

    while True:
        html = get_html(url)
        soup = BeautifulSoup(html, "lxml")
        print(get_tasks(soup))

        if input("Enter q for stop or enter to continue: ") == "q":
            break
        else:
            a += 1
            url = 'https://www.fl.ru/projects/' + '?page='+ str(a) + '&kind=5'
            print("=" * 40)
main()
