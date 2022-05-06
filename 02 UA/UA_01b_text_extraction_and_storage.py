from bs4 import BeautifulSoup
import requests
import codecs
from datetime import datetime
import pandas as pd

# Replace these variables accordingly:
# (n, section, base_url, class_in_var_url_list, class_in_var_parafs,
# class_in_var_headline, class_in_var_time, class_in_var_link, )

n = 40  # n is the number of pages the section of every subject has
section = 'history'
base_url = 'https://www.istpravda.com.ua'
section_in_url = base_url + '/articles/page_'

for i in range(1, n + 1):
    try:
        article_log = pd.read_excel(f"UA_{section}_log.xlsx")
        publ_dates = article_log['publ_dates'].tolist()
        time_extracted = article_log['time_extracted'].tolist()
        headlines = article_log['headlines'].tolist()
        links = article_log['links'].tolist()
    except FileNotFoundError:
        publ_dates = []
        time_extracted = []
        headlines = []
        links = []

    page_url = section_in_url + str(i)
    print(page_url)
    html_text = requests.get(page_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    url_list = soup.find_all('h3', class_="article__title")
    print(f"Page {i} out of {n}")

    for url in url_list:
        # I introduce this if statement because there's problematic articles, i.e. having href=string
        if url.a['href'].startswith('/'):
            url = base_url + url.a['href']
            print(url)
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            try:
                parafs = soup.find('div', class_="post__text").find_all('p', class_=False)  #Can be empty list, therefore potential AttributeError
                for paraf in parafs:
                    with codecs.open(f"UA_{section}_text.txt", "a", "utf-16") as acum_text:
                        acum_text.write(paraf.text + "\n")

                headline = soup.find('h1', class_='post__title').text
                publ_date = soup.find('div', class_='post__date').text
                link = soup.find('div', class_='post__text')['data-io-article-url']
                headlines.append(headline)
                publ_dates.append(publ_date)
                time_extracted.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                links.append(link)

            except AttributeError:
                continue
        else:
            continue

    # the website renders three popular news from the current day (and not the day we are using)
    # at the bottom of each page, therefore we delete them
    """
    columns = [publ_dates, time_extracted, headlines, links]
    for column in columns:
        for j in range(3):
            column.pop()
    """

    article_log = pd.DataFrame(
        {"publ_dates": publ_dates, "time_extracted": time_extracted, "headlines": headlines, "links": links})
    article_log.to_excel(f'UA_{section}_log.xlsx', index=False)

    with codecs.open(f"UA_{section}_text.txt", "a", "utf-16") as acum_text:
        acum_text.write(f"\nEnd of page {i} \n\n")
# Alarm
import playsound
playsound.playsound(r"C:\Users\kebc_\PycharmProjects\Project1\UA\anarchy.mp3", True)
