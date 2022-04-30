from bs4 import BeautifulSoup
import requests
import codecs

# As of Dec 7, 2021, the "kraj" section has 589 pages.
# As of Dec 9, 2021, the "swiat" section has 315 pages.
# As of Dec 9, 2021, the "kultura" section has 256 pages.
# As of Dec 9, 2021, the "gospodarka" section has 56 pages.

headlines = []
dates = []
time_extracted = []

num_skipped_pages = 0

for i in range(1, 56):
    page_url = f"https://krytykapolityczna.pl/gospodarka/page/{i}/"
    html_text = requests.get(page_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    url_list = soup.find_all('header', class_="post-entry-header")
    print(f"Page {i}")
    if i <= 200:
        part = 1
    elif 200 < i <= 400:
        part = 2
    else:
        part = 3
    num_url = 0
    for url in url_list:
        num_url += 1
        print(num_url)
        url = url.h2.a['href']
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        # There are some problematic articles that don't comply with the structure used. E.g. https://krytykapolityczna.pl/kraj/od-redakcji/
        try:
            parafs = soup.find('div', class_="single-post-content").find_all('p', class_=False)
            # We need a try, except because some pages include tags like <strong> or <em>
            parafs.pop()
            for paraf in parafs:
                with codecs.open(f"gospodarka_text_part_{part}.txt", "a", "utf-16") as acum_text:
                    acum_text.write(paraf.text + " ")
            with codecs.open(f"gospodarka_text_part_{part}.txt", "a", "utf-16") as acum_text:
                acum_text.write("\n")
        except:
            num_skipped_pages += 1

print(num_skipped_pages)

"""""
# Extraction of links from each page. Using gazeta.pl
page_url = "https://wiadomosci.gazeta.pl/wiadomosci/0,114883.html?str=1_19834543"
html_text = requests.get(page_url).text
soup = BeautifulSoup(html_text, 'html.parser')
links = soup.find_all('article', class_="article")
for link in links:
    print(link.a['href'])

# Extraction of text from each article
article_url = "https://wiadomosci.gazeta.pl/wiadomosci/7,114883,27813403,w-niemczech-dyskusja-nt-rozmowy-merkel-z-lukaszenka-fatalne.html"

html_text = requests.get(article_url).text
soup = BeautifulSoup(html_text, 'html.parser')
# parafs = soup.find('div', class_="bottom_section")
parafs = soup.find_all('p', class_="art_paragraph")
for paraf in parafs:
    print(paraf.text)
"""""