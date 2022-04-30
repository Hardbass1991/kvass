from datetime import date, timedelta
current_date = date.today()
#current_date += timedelta(days=-180)
from bs4 import BeautifulSoup
import requests
import codecs
from datetime import datetime
import pandas as pd
import os

# Replace these variables accordingly:
n = 250  # n is the number of pages the section of every subject has
section = 'economy'
section_in_url = 'https://www.epravda.com.ua/rus/archives/date_'

for i in range(1, n+1):
    try:
        article_log = pd.read_excel(f"RU_{section}_log.xlsx")
        publ_dates = article_log['publ_dates'].tolist()
        time_extracted = article_log['time_extracted'].tolist()
        headlines = article_log['headlines'].tolist()
        links = article_log['links'].tolist()
    except FileNotFoundError:
        publ_dates = []
        time_extracted = []
        headlines = []
        links = []

    day = current_date.strftime('%d')
    month = current_date.strftime('%m')
    year = current_date.strftime('%Y')

    page_url = section_in_url + day + month + year + '/'
    print(page_url)
    html_text = requests.get(page_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    url_list = soup.find_all('div', class_="article__title")
    print(f"Page {i} out of {n}")

    for url in url_list:
        # I introduce this if statement because there's problematic articles, i.e. having href=string
        if url.a['href'].startswith('/'):
            url = 'https://www.epravda.com.ua' + url.a['href']
            print(url)
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            try:
                subtitle = soup.find('div', class_='post__subtitle').text  # Susceptible to AttributeError
                is_ukrainian_0 = subtitle.index('(укр)')  # Susceptible to ValueError
            except AttributeError as e:
                print(e)
                parafs = soup.find('div', class_="post__text").find_all('p', class_=False)
                # The last element in the list is the credits, so we pop it.
                parafs.pop()
                for paraf in parafs:
                    with codecs.open("test.txt", "a", "utf-16") as test_text:
                        test_text.write(paraf.text + "\n")
                count_ukrainian_i = 0
                is_ukrainian_1 = False
                with codecs.open("test.txt", "a", "utf-16") as test_text:
                    for line in test_text:
                        if 'і' in line:
                            count_ukrainian_i += 1
                        if count_ukrainian_i > 0:
                            is_ukrainian_1 = True
                            break
                if not is_ukrainian_1:
                    with codecs.open(f"RU_{section}_text.txt", "a", "utf-16") as acum_text:
                        with codecs.open("test.txt", "r", "utf-16") as test_text:
                            acum_text.append(test_text + "\n")

                    headline = soup.find('h1', class_="post__title").text
                    publ_date = soup.find('div', class_='post__time').text
                    link = soup.find('div', class_='post__text')['data-io-article-url']
                    headlines.append(headline)
                    publ_dates.append(publ_date)
                    time_extracted.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    links.append(link)
                else:
                    os.remove("test.txt")
                    continue
        else:
            continue

    columns = [publ_dates, time_extracted, headlines, links]
    for column in columns:
        for j in range(3):
            column.pop()

    article_log = pd.DataFrame({"publ_dates": publ_dates, "time_extracted": time_extracted, "headlines": headlines, "links": links})
    article_log.to_excel(f'RU_{section}_log.xlsx', index=False)

    current_date += timedelta(days=-1)
    with codecs.open(f"RU_{section}_text.txt", "a", "utf-16") as acum_text:
        acum_text.write(f"\nEnd of page {i} \n\n")
# Alarm
import playsound
playsound.playsound(r"C:\Users\kebc_\PycharmProjects\Project1\RU\anarchy.mp3", True)