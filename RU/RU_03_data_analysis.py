import pickle
import csv
import pandas as pd

# a_file = open("sample.csv", "w", encoding="utf-16", newline='')

with open('RU_dict_desc.pickle', 'rb') as handle:
    ru_dict = pickle.load(handle)
    ru_dict = {k: v for k, v in ru_dict.items() if v >= 600}
    dict_acum_df = pd.DataFrame({"keys": list(ru_dict.keys()), "values": list(ru_dict.values())})

for i in range(18, 0, -1):
    with open(f'RU_dict_{i * 100}_articles.pickle', 'rb') as handle:
        ru_dict = pickle.load(handle)
        ru_dict = {k: v for k, v in sorted(ru_dict.items(), key=lambda item: item[1], reverse=True)}
        dict_i_df = pd.DataFrame({"keys": list(ru_dict.keys()), "values": list(ru_dict.values())})

    dict_acum_df = dict_acum_df.merge(dict_i_df, how='left', on='keys')

dict_acum_df.columns.values[1] = "full"
for i in range(2, 20):
    dict_acum_df.columns.values[i] = f'{(20 - i)*100}_articles'

print(dict_acum_df)
dict_acum_df.to_csv("dict_acum_df.csv", encoding="utf-16")
"""
writer = csv.writer(a_file)

for key, value in ru_dict.items():
    writer.writerow([key, value])

a_file.close()
"""