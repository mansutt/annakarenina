import os
import string


def preprocessing(input_text):
    clean_lines = []
    for line in input_text:
        if line.startswith('PART'):
            input_text.remove(line)
        elif line.startswith('Chapter'):
            input_text.remove(line)
        elif line.startswith('\n'):
            input_text.remove(line)
    for line in input_text:
        clean_lines.append(line.strip())
    # (messes up text if in first for loop)
    clean_lines = [i.lower() for i in clean_lines]
    clean_lines2 = []
    for li in clean_lines:
        for letter in li:
            if letter in string.punctuation:
                li = li.replace(letter, '')
        clean_lines2.append(li)
    clean_lines3 = []
    clean_lines3 = ' '.join(clean_lines2).split(' ')
    wc_str = ' '.join(clean_lines3)
    return wc_str


#####

with open(os.path.join('..', 'text', 'ak_p1.txt'), 'r', encoding='utf-8') as file:
    ak_p1 = file.readlines()

clean_text_p1 = preprocessing(ak_p1)

with open(os.path.join('..', 'text', 'ak_p1_test.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p1)


# iterate over dedicated folder with each part of the book
