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


def character_count(part, name):
    def occurrences(word):
        return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), part))
        # (efficient code to count occurrences of a word in a long string by user "Amber" on StackOverflow)

    main_chars = {}

    konstantin_levin = occurrences('konstantin') + occurrences('levin') + occurrences('kostya') - \
                       occurrences('konstantin levin')
    main_chars['Konstantin Levin'] = konstantin_levin

    anna_karenina = occurrences('anna') + occurrences('arkadyevna') - occurrences('anna arkadyevna')
    main_chars['Anna Karenina'] = anna_karenina

    alexey_vronsky = occurrences('alexey kirillovich') + occurrences('vronsky') - occurrences('alexey vronsky')
    # difficult because of 2 characters named Alexey -> Alexey Vronsky and Alexey Karenin
    main_chars['Alexey Vronsky'] = alexey_vronsky

    stepan_oblonsky = occurrences('stepan arkadyevitch') + occurrences('stiva') + occurrences('oblonsky') - \
                      occurrences('stiva oblonsky')
    main_chars['Stepan Oblonsky'] = stepan_oblonsky

    darya_oblonskaya = occurrences('darya') + occurrences('dolly') + occurrences('oblonskaya') - \
                       occurrences('darya oblonskaya')
    main_chars['Darya Oblonskaya'] = darya_oblonskaya

    alexey_karenin = occurrences('alexey karenin') + occurrences('alexey alexandrovitch')
    main_chars['Alexey Karenin'] = alexey_karenin

    alexey_unclear = occurrences('alexey')
    main_chars['Alexey (unclear)'] = alexey_unclear

    all_parts['Part ' + str(name)] = main_chars


character_count(ak_p1_lem, 1)
character_count(ak_p2_lem, 2)
character_count(ak_p3_lem, 3)
character_count(ak_p4_lem, 4)
character_count(ak_p5_lem, 5)
character_count(ak_p6_lem, 6)
character_count(ak_p7_lem, 7)
character_count(ak_p8_lem, 8)

df = pd.DataFrame(all_parts)
df.plot(kind='bar', stacked=True, legend='reverse')
plt.gcf().subplots_adjust(bottom=0.3)  # prevents cut-off of x labels

plt.savefig('characters.png', dpi=400, bbox_inches='tight')
