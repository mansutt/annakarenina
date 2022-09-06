import os
import re
from matplotlib import pyplot as plt
import pandas as pd

with open(os.path.join('..', 'text', 'lemmatized', 'ak_complete_lem.txt'), 'r', encoding='utf-8') as file:
    ak_complete_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p1_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p1_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p2_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p2_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p3_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p3_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p4_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p4_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p5_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p5_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p6_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p6_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p7_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p7_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p8_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p8_lem = file.read()

all_parts = {}


def location_count(part, name):
    def occurrences(word):
        return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), part))
        # (efficient code to count occurrences of a word in a long string by user "Amber" on StackOverflow)

    places = {}

    places['Moscow'] = occurrences('moscow')
    places['St. Petersburg'] = occurrences('petersburg')
    places['Pokrovskoe'] = occurrences('pokrovskoe')
    places['Vozdvizhenskoe'] = occurrences('vozdvizhenskoe')

    all_parts['Part ' + str(name)] = places


location_count(ak_p1_lem, 1)
location_count(ak_p2_lem, 2)
location_count(ak_p3_lem, 3)
location_count(ak_p4_lem, 4)
location_count(ak_p5_lem, 5)
location_count(ak_p6_lem, 6)
location_count(ak_p7_lem, 7)
location_count(ak_p8_lem, 8)

df = pd.DataFrame(all_parts)
df.plot(kind='bar', stacked=True, legend='reverse')
plt.gcf().subplots_adjust(bottom=0.3)  # prevents cut-off of x labels

plt.savefig('locations.png', dpi=400, bbox_inches='tight')
