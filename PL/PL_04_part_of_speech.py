from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()
word = parser.fetch('klient', 'polish')
definition = word[0]['definitions'][0]['text'][1]
part_of_speech = word[0]['definitions'][0]['partOfSpeech']
print(part_of_speech, definition)