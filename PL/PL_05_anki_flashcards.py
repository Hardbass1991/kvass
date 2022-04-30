import genanki
import pandas as pd

my_model = genanki.Model(
  1243799134,
  'Simple Model with Media',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'MyMedia'},                                  # ADD THIS
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}<br>{{MyMedia}}',              # AND THIS
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])
my_deck = genanki.Deck(
  1243799134,
  'PL1')

import os
words_csv = pd.read_excel("prueba.xlsx", header=None)
words = words_csv[0].tolist()
defs = words_csv[1].tolist()

# Create a dictionary to link every word to its definition
definition = {}
for i in range(len(words)):
  definition[words[i]] = defs[i]

os.chdir(os.getcwd()+"/W9")
img_files = os.listdir(os.getcwd())

my_package = genanki.Package(my_deck)
my_package.media_files = img_files
print(img_files)

x = 0
for word in words:
  img_name = word
  try:
    first_letter = img_name.index("]") + 2
    img_name = img_name[first_letter:]
    last_letter = img_name.index("[") - 1
    img_name = img_name[:last_letter]
    img_file = [x for x in img_files if x.startswith(img_name)][0]
  except ValueError:
    img_file = [x for x in img_files if x.startswith(img_name)][0]
  print(word, definition[word], img_file)

  img_file = f'<img src="{img_file}">'
  side_A = word + "\n\n" + img_file
  print(side_A)
  my_note = genanki.Note(
    model=my_model,
    fields=[word, definition[word], img_file])
  my_deck.add_note(my_note)

os.chdir("../")
genanki.Package(my_deck).write_to_file('PL0.apkg')
