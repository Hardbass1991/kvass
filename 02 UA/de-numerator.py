import codecs
sections = ['politics', 'economy', 'history']

for section in sections:
    with codecs.open(f"UA_{section}_text.txt", "r", "utf-16") as text:
        for line in text.readlines():
            if 'End of page' in line:
                continue
            else:
                with codecs.open(f"UA_{section}_text_denumerated.txt", "a", "utf-16") as denumerated_text:
                    denumerated_text.write(line)
