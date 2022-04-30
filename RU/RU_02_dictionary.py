import stanza
# stanza.download('ru') # download Russian model
nlp = stanza.Pipeline('ru') # initialize Russian neural pipeline
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
import time
start_time = time.time()

with codecs.open("economic_text_part_3.txt", "r", "utf-16") as economic_text:
    num_word = 0
    num_line = 0
    with open('RU_dict.pickle', 'rb') as handle:
        ru_dict = pickle.load(handle)

    for line in economic_text:
        doc = nlp(line)
        num_line += 1

        for sentence in doc.sentences:
            for word in sentence.words:
                if word.pos == "NOUN" or word.pos == "ADJ" or word.pos == "VERB" or word.pos == "ADV":
                    num_word += 1
                    ru_dict[word.lemma] = ru_dict.get(word.lemma, 0) + 1

        with open('RU_dict.pickle', 'wb') as handle:
            pickle.dump(ru_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

        if num_line % 100 == 0:
            print(f'Line {num_line + 1200}')

            from shutil import copyfile
            copyfile('RU_dict.pickle', f'RU_dict_{num_line + 1200}_articles.pickle')


with open('RU_dict.pickle', 'rb') as handle:
    ru_dict = pickle.load(handle)
ru_dict = {k: v for k, v in sorted(ru_dict.items(), key=lambda item: item[1], reverse=True)}
# print(ru_dict)
with open('RU_dict_desc.pickle', 'wb') as handle:
    pickle.dump(ru_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
print(ru_dict)
print("--- %s seconds ---" % (time.time() - start_time))




