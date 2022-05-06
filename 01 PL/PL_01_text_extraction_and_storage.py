from bs4 import BeautifulSoup
import requests
import codecs
from datetime import datetime
import pandas as pd

# As of April 28, 2022, the Economy ("gospodarka") section has 61 pages.
# As of April 28, 2022, the Culture ("kultura") section has 265 pages.
# As of April 28, 2022, the Country ("kraj") section has 607 pages.

# [(61, 'economy', 'gospodarka'), (80, 'world', 'swiat'), (70, 'country', 'kraj'), (60, 'culture', 'kultura')]

# Replace these variables accordingly:
n = 60  # n is the number of pages the section of every subject has
section = 'culture'
section_in_url = 'kultura'

for i in range(1, n+1):
    try:
        article_log = pd.read_excel(f"PL_{section}_log.xlsx")
        publ_dates = article_log['publ_dates'].tolist()
        time_extracted = article_log['time_extracted'].tolist()
        headlines = article_log['headlines'].tolist()
    except FileNotFoundError:
        publ_dates = []
        time_extracted = []
        headlines = []

    page_url = f"https://krytykapolityczna.pl/{section_in_url}/page/{i}/"
    html_text = requests.get(page_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    url_list = soup.find_all('header', class_="post-entry-header")
    print(f"Page {i} out of {n}")
    # We section some content in batches to make later processing less difficult
    if i <= 200:
        part = 1
    elif 200 < i <= 400:
        part = 2
    else:
        part = 3

    for url in url_list:
        url = url.h2.a['href']
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        # There are some problematic articles that don't comply with the structure used. E.g. https://krytykapolityczna.pl/kraj/od-redakcji/
        # We need a try, except because some pages include tags like <strong> or <em>
        try:
            parafs = soup.find('div', class_="single-post-content").find_all('p', class_=False)
            # The last element in the list is the credits, so we pop it.
            parafs.pop()
            for paraf in parafs:
                with codecs.open(f"PL_{section}_text_part_{part}.txt", "a", "utf-16") as acum_text:
                    acum_text.write(paraf.text + "\n")
            headline = soup.find('h1', class_="entry-title").text
            publ_date = soup.find('time')['datetime']
            headlines.append(headline)
            publ_dates.append(publ_date)
            time_extracted.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        except:
            headlines.append('')
            publ_dates.append('')
            time_extracted.append('')

    article_log = pd.DataFrame({"publ_dates": publ_dates, "time_extracted": time_extracted, "headlines": headlines})
    article_log.to_excel(f'PL_{section}_log.xlsx', index=False)
