from wiktionaryparser import WiktionaryParser
import pandas as pd

sections = ['economy', 'politics', 'history']
country = 'UA'
language = 'ukrainian'

for section in sections:
    word_list = pd.read_excel(f"{country}_{section}_ranking.xlsx", header=0)
    words = word_list['words'].tolist()

    defs = []
    parts_of_speech = []
    i = 1
    n = len(words)
    parser = WiktionaryParser()
    for word in words:
        print(f"{word}, word {i} of {n}")
        try:
            word = parser.fetch(word, language)
            definition = word[0]['definitions'][0]['text'][1]
            part_of_speech = word[0]['definitions'][0]['partOfSpeech']
            defs.append(definition)
            parts_of_speech.append(part_of_speech)
        except IndexError:
            defs.append("")
            parts_of_speech.append("")
            i += 1
            continue
        i += 1

    words_and_defs_df = pd.DataFrame({"words": words, "part of speech": parts_of_speech, "defs": defs})
    words_and_defs_df.to_excel(f"{country}_{section}_words_and_defs.xlsx", index=None)

    print(f'Section {section} finished')
