import stanza
# stanza.download('pl') # download Polish model
nlp = stanza.Pipeline('pl') # initialize Polish neural pipeline
# TEST SETS
"""
doc = nlp("На это американцы явно не рассчитывали. Министерство финансов США подверглось давлению собственных концернов — не в последнюю очередь концерном Boeing.")
noun = nlp("кость кости костью костей костям костями костях ")
adj = nlp("костяной костяного костяному костяным костяном костяное костяная костяную")
verb = nlp("пренебрегаю пренебрегаешь пренебрегает пренебрегаем пренебрегаете пренебрегают буду пренебрегать пренебрегай пренебрегал пренебрегала пренебрегало пренебрегали")
verb_perfective = nlp ("скажу скажешь скажет скажем скажете скажут скажи сказало")
"""

import codecs
import pickle
from datetime import datetime

section = 'economy'

log_info = ''
origin_file = f'PL_{section}_text_part_1.txt'
log_info += origin_file
start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log_info += ' ' + start_time

pl_dict = {}

with codecs.open(origin_file, "r", "utf-16") as text:
    num_lines = len(text.readlines())
    print(num_lines)

with codecs.open(origin_file, "r", "utf-16") as text:
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

        if num_line % 200 == 0:
            print(f'Line {num_line} out of {num_lines}')
            """""
            from shutil import copyfile
            copyfile('PL_economy_dict.pickle', f'PL_economy_dict_{num_line}_articles.pickle')
            """""
            end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_info += ' ' + end_time
            with codecs.open(f'PL_{section}_log.txt', "a", "utf-16") as text:
                text.write(log_info + '\n')
        with open(f'PL_{section}_dict.pickle', 'rb') as handle:
            pl_dict = pickle.load(handle)



with open(f'PL_{section}_dict.pickle', 'rb') as handle:
    pl_dict = pickle.load(handle)
pl_dict = {k: v for k, v in sorted(pl_dict.items(), key=lambda item: item[1], reverse=True)}
# print(ru_dict)
with open(f'PL_{section}_dict_desc.pickle', 'wb') as handle:
    pickle.dump(pl_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
print(pl_dict)





