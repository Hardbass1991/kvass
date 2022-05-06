from datetime import date, timedelta
current_date = date.today()
# current_date += timedelta(days=-240)
from bs4 import BeautifulSoup
import requests
import codecs
from datetime import datetime
import pandas as pd
import os

# Replace these variables accordingly:
# (n, section, base_url, class_in_var_url_list, class_in_var_parafs,
# class_in_var_headline, class_in_var_time, class_in_var_link, )

# [(181, 'economy', 'https://www.epravda.com.ua', "article__title", "post__text", "post__title", 'post__time', 'post__text'),
# (145, 'politics', 'https://www.pravda.com.ua', "article_header", "post_text", 'post_title', 'post_time', 'post_text'), ]

n = 200  # n is the number of pages the section of every subject has
section = 'politics'
base_url = 'https://www.pravda.com.ua'
section_in_url = base_url + '/rus/archives/date_'

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
    url_list = soup.find_all('div', class_="article_header")
    print(f"Page {i} out of {n}")

    for url in url_list:
        # I introduce this if statement because there's problematic articles, i.e. having href=string
        if url.a['href'].startswith('/'):
            url = base_url + url.a['href']
            print(url)
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')

            try:
                parafs = soup.find('div', class_="post_text").find_all('p', class_=False)  #Can be empty list, therefore potential AttributeError
                # The last element in the list is the credits, so we pop it.
                parafs.pop()
                for paraf in parafs:
                    # print(paraf.text)
                    with codecs.open("test.txt", "a", "utf-16") as test_text:
                        test_text.write(paraf.text + "\n")
                count_ukrainian_i = 0
                is_ukrainian_1 = False
                with codecs.open("test.txt", "r", "utf-16") as test_text:
                    lines = test_text.readlines()
                    for line in lines:
                        if 'і' in line:
                            count_ukrainian_i += 1
                        if count_ukrainian_i > 0:
                            is_ukrainian_1 = True
                            break
                if not is_ukrainian_1:
                    with codecs.open("test.txt", "r", "utf-16") as test_text:
                        lines = test_text.read()
                    with codecs.open(f"RU_{section}_text.txt", "a", "utf-16") as acum_text:
                        acum_text.write(lines)

                    headline = soup.find('h1', class_='post_title').text
                    publ_date = soup.find('div', class_='post_time').text
                    link = soup.find('div', class_='post_text')['data-io-article-url']
                    headlines.append(headline)
                    publ_dates.append(publ_date)
                    time_extracted.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    links.append(link)
                    os.remove("test.txt")
                else:
                    os.remove("test.txt")
                    continue
            except (FileNotFoundError, IndexError, AttributeError):
                continue
        else:
            continue

    columns = [publ_dates, time_extracted, headlines, links]
    for column in columns:
        for j in range(3):
            column.pop()

    article_log = pd.DataFrame(
        {"publ_dates": publ_dates, "time_extracted": time_extracted, "headlines": headlines, "links": links})
    article_log.to_excel(f'RU_{section}_log.xlsx', index=False)

    current_date += timedelta(days=-1)
    with codecs.open(f"RU_{section}_text.txt", "a", "utf-16") as acum_text:
        acum_text.write(f"\nEnd of page {i} \n\n")

    # We get the size of the output file, which should reach should slightly surpass 20000 kb
    file_size_kb = os.path.getsize(f"RU_{section}_text.txt") / 1024
    print(f'File size: {file_size_kb} kb')
    if file_size_kb > 20000:
        break
# Alarm
import playsound

playsound.playsound(r"C:\Users\kebc_\PycharmProjects\Project1\RU\anarchy.mp3", True)
