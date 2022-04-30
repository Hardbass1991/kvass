import pickle
import csv
import pandas as pd

with open('PL_kraj_dict_desc.pickle', 'rb') as handle:
    pl_dict = pickle.load(handle)
    pl_dict = {k: v for k, v in pl_dict.items() if v >= 100}
    keys = list(pl_dict.keys())
    values = list(pl_dict.values())
"""
    import requests
    for i in keys:
        page_url = f"https://krytykapolityczna.pl/kraj/page/{i}/"
        html_text = requests.get(page_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        url_list = soup.find_all('header', class_="post-entry-header")
"""
dict_acum_kraj_df = pd.DataFrame({"keys": keys, "values": values})

"""
for i in range(18, 0, -1):
    with open(f'pl_dict_{i * 100}_articles.pickle', 'rb') as handle:
        pl_dict = pickle.load(handle)
        pl_dict = {k: v for k, v in sorted(pl_dict.items(), key=lambda item: item[1], reverse=True)}
        dict_i_df = pd.DataFrame({"keys": list(pl_dict.keys()), "values": list(pl_dict.values())})

    dict_acum_df = dict_acum_df.merge(dict_i_df, how='left', on='keys')

dict_acum_df.columns.values[1] = "full"
for i in range(2, 20):
    dict_acum_df.columns.values[i] = f'{(20 - i)*100}_articles'
"""

print(dict_acum_kraj_df)
dict_acum_kraj_df.to_csv("dict_acum_kraj_df.csv", encoding="utf-16")
"""
writer = csv.writer(a_file)

for key, value in pl_dict.items():
    writer.writerow([key, value])

a_file.close()
"""