import stanza
nlp = stanza.Pipeline('pl') # initialize Polish neural pipeline
# TEST SETS

import codecs
import pickle
from datetime import datetime
import pandas as pd

section = 'world'

origin_file = f'PL_{section}_text_part_1.txt'
start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with codecs.open(origin_file, "r", "utf-16") as text:
    num_lines = len(text.readlines())
    print(num_lines)

with codecs.open(origin_file, "r", "utf-16") as text:

    try:
        dictionary_log = pd.read_excel(f"PL_{section}_dict_log.xlsx")
        lines_completed = dictionary_log['lines_completed'].tolist()
        times_ended = dictionary_log['times_ended'].tolist()

    except FileNotFoundError:
        lines_completed = []
        times_ended = []

    try:
        with open(f'PL_{section}_dict.pickle', 'rb') as handle:
            pl_dict = pickle.load(handle)
    except FileNotFoundError:
        pl_dict = {}

    num_line = 0
    for line in text:
        doc = nlp(line)
        num_line += 1
        for sentence in doc.sentences:
            for word in sentence.words:
                if word.pos == "NOUN" or word.pos == "ADJ" or word.pos == "VERB" or word.pos == "ADV":
                    pl_dict[word.lemma] = pl_dict.get(word.lemma, 0) + 1

        with open(f'PL_{section}_dict.pickle', 'wb') as handle:
            pickle.dump(pl_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

        if num_line % 10 == 0:
            print(f'Line {num_line} out of {num_lines}')
        if num_line % 500 == 0:
            lines_completed.append(num_line)
            times_ended.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            dictionary_log = pd.DataFrame({"lines_completed": lines_completed, "times_ended": times_ended})
            dictionary_log.to_excel(f'PL_{section}_dict_log.xlsx', index=False)

with open(f'PL_{section}_dict.pickle', 'rb') as handle:
    pl_dict = pickle.load(handle)
pl_dict = {k: v for k, v in sorted(pl_dict.items(), key=lambda item: item[1], reverse=True)}
# print(ru_dict)
with open(f'PL_{section}_dict_desc.pickle', 'wb') as handle:
    pickle.dump(pl_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
print(pl_dict)
