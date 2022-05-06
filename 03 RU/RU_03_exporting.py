import pandas as pd
import pickle
import json
import codecs

sections = ['economy', 'politics']
country = 'RU'

for section in sections:
    # Check the log to find our infrequency coefficient (IC) (IC is the number of words that, on average,
    # you need to analyze to find an occurrence of the word)
    with codecs.open(f'{country}_{section}_text.txt', "r", "utf-16") as text:
        data = text.read()
        words = data.split()
        num_of_words = 0
        for word in words:
            if word.isalpha():
                num_of_words += 1

    article_log = pd.read_excel(f"{country}_{section}_log.xlsx", header=None)
    num_of_articles = len(article_log[0].tolist()) - 1
    print(num_of_articles, num_of_words, section)
    # We arbitrarily set
    ic = 10000
    # And calculate a threshold. The lower the ic, the higher the threshold of occurrences
    # And therefore the most frequently a word needs to appear to be included in the output array
    # For instance, ic = 1 implies that every word has to be an occurrence of the word analyzed.
    # On the other hand, ic = 10 implies that the word has to appear, on average, once for every 10 words analyzed
    threshold = num_of_words / ic

    # We load the pickle
    with open(f'{country}_{section}_dict_desc.pickle', 'rb') as handle:
        dict = pickle.load(handle)
        dict = {k: v for k, v in dict.items() if v >= round(threshold) and k.isalpha()}
        keys = list(dict.keys())
        values = list(dict.values())

    # We export an .xlsx file for a further task (Output 1)
    ranking_df = pd.DataFrame({"words": keys, "occurrences": values})
    ranking_df.to_excel(f"{country}_{section}_ranking.xlsx", index=False)

    # We save a modified .pickle file to convert it to JSON format
    with open(f'{country}_{section}_dict_desc_to_json.pickle', 'wb') as handle:
        pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # We load the modified .pickle file
    with open(f'{country}_{section}_dict_desc_to_json.pickle', 'rb') as handle:
        obj = pickle.load(handle)
    # We convert pickle object to json object
    json_obj = json.loads(json.dumps(obj, default=str))

    # write the json file
    with open(f'{country}_{section}_ranking' + '.json', 'w', encoding='utf-16') as outfile:
        json.dump(json_obj, outfile, ensure_ascii=False, indent=4)










