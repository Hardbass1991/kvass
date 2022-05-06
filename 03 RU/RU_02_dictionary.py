import stanza
# activate venv
nlp = stanza.Pipeline('ru') # initialize Russian neural pipeline
# TEST SETS

import codecs
import pickle
from datetime import datetime
import pandas as pd

section = 'politics'
country = 'RU'

origin_file = f'{country}_{section}_text.txt'

with codecs.open(origin_file, "r", "utf-16") as text:
    num_lines = len(text.readlines())
    print(num_lines)

with codecs.open(origin_file, "r", "utf-16") as text:
    try:
        dictionary_log = pd.read_excel(f"{country}_{section}_dict_log.xlsx")
        lines_completed = dictionary_log['lines_completed'].tolist()
        times_ended = dictionary_log['times_ended'].tolist()
    except FileNotFoundError:
        lines_completed = []
        times_ended = []

    try:
        with open(f'{country}_{section}_dict.pickle', 'rb') as handle:
            dict = pickle.load(handle)
    except FileNotFoundError:
        dict = {}

    num_line = 0
    for line in text:
        doc = nlp(line)
        num_line += 1
        for sentence in doc.sentences:
            for word in sentence.words:
                if word.pos == "NOUN" or word.pos == "ADJ" or word.pos == "VERB" or word.pos == "ADV":
                    dict[word.lemma] = dict.get(word.lemma, 0) + 1

        with open(f'{country}_{section}_dict.pickle', 'wb') as handle:
            pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

        if num_line % 10 == 0:
            print(f'Line {num_line} out of {num_lines}')
        if num_line % 500 == 0:
            lines_completed.append(num_line)
            times_ended.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            dictionary_log = pd.DataFrame({"lines_completed": lines_completed, "times_ended": times_ended})
            dictionary_log.to_excel(f'{country}_{section}_dict_log.xlsx', index=False)

        if num_line >= 20000:
            break


with open(f'{country}_{section}_dict.pickle', 'rb') as handle:
    dict = pickle.load(handle)
dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

with open(f'{country}_{section}_dict_desc.pickle', 'wb') as handle:
    pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)