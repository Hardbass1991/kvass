import codecs
section = 'history'
num_pages = 0

with codecs.open(f"UA_{section}_text.txt", "r", "utf-16") as text:
    for line in text.readlines():
        if line.startswith('End of page'):
            num_pages += 1
            print(f'Page {num_pages}')
        with codecs.open(f"UA_{section}_text_trimmed.txt", "a", "utf-16") as trimmed_text:
            trimmed_text.write(line)
        if num_pages >= 40:
            break