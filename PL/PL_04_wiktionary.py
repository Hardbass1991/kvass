from wiktionaryparser import WiktionaryParser
import pandas as pd

words_csv = pd.read_excel("word_list.xlsx", header=0)
words = words_csv['words'].tolist()
print(words)

defs = []
i = 1
n = len(words)
parser = WiktionaryParser()
for word in words:
    print(f"{word}, word {i} of {n}")
    try:
        word = parser.fetch(word, 'polish')
        definition = word[0]['definitions'][0]['text'][1]
        defs.append(definition)
    except IndexError:
        defs.append("")
        i += 1
        continue
    i += 1

words_and_defs_df = pd.DataFrame({"words": words, "defs": defs})
words_and_defs_df.to_excel("words_and_defs_df.xlsx")