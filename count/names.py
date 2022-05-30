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


# Efficient code to count occurrences of a word in a long string by user "Amber" on StackOverflow:

def occurrences(word):
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), ak_complete_lem))


# counting occurrences of main characters in whole book and adding to dictionary

# main_chars = {}
#
# anna_karenina = occurrences('anna') + occurrences('arkadyevna') - occurrences('anna arkadyevna')
# main_chars['Anna Karenina'] = anna_karenina
#
# alexei_vronsky = occurrences('alexey kirillovich') + occurrences('vronsky') - occurrences('alexey vronsky')
# # difficult because of 2 characters named Alexey -> Alexey Vronsky and Alexey Karenin
# main_chars['Alexey Vronsky'] = alexei_vronsky
#
# alexey_unclear = occurrences('alexey')
# main_chars['Alexey (unclear)'] = alexey_unclear
#
# stepan_oblonsky = occurrences('stepan arkadyevitch') + occurrences('stiva') + occurrences('oblonsky')
# main_chars['Stepan Oblonsky'] = stepan_oblonsky
#
# darya_oblonskaya = occurrences('darya') + occurrences('dolly') + occurrences('oblonskaya') - \
#                    occurrences('darya oblonskaya')
# main_chars['Darya Oblonskaya'] = darya_oblonskaya
#
# alexey_karenin = occurrences('alexey karenin') + occurrences('alexey alexandrovitch')
# main_chars['Alexey Karenin'] = alexey_karenin
#
# konstantin_levin = occurrences('konstantin') + occurrences('levin') + occurrences('kostya') - \
#                    occurrences('konstantin levin')
# main_chars['Konstantin Levin'] = konstantin_levin
#
# # barplotting
# keys = main_chars.keys()
# values = main_chars.values()
#
# plt.bar(keys, values)
# plt.xticks(rotation=45)
# plt.savefig('main_characters_complete.png', dpi=400, bbox_inches='tight')

# todo: combine multiple expressions to one character/topic so program can differentiate between different names

# print(main_chars)


# anna = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('anna'), ak_complete_lem))
# karenina = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('karenina'), ak_complete_lem))
# anna_karenina = anna + karenina

all_parts = {}

def character_count(part, name):
    def occurrences_2(word):
        return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), part))

    main_chars = {}

    anna_karenina = occurrences_2('anna') + occurrences_2('arkadyevna') - occurrences_2('anna arkadyevna')
    main_chars['Anna Karenina'] = anna_karenina

    alexey_vronsky = occurrences_2('alexey kirillovich') + occurrences_2('vronsky') - occurrences_2('alexey vronsky')
    # difficult because of 2 characters named Alexey -> Alexey Vronsky and Alexey Karenin
    main_chars['Alexey Vronsky'] = alexey_vronsky

    alexey_unclear = occurrences_2('alexey')
    main_chars['Alexey (unclear)'] = alexey_unclear

    stepan_oblonsky = occurrences_2('stepan arkadyevitch') + occurrences_2('stiva') + occurrences_2('oblonsky')
    main_chars['Stepan Oblonsky'] = stepan_oblonsky

    darya_oblonskaya = occurrences_2('darya') + occurrences_2('dolly') + occurrences_2('oblonskaya') - \
                       occurrences_2('darya oblonskaya')
    main_chars['Darya Oblonskaya'] = darya_oblonskaya

    alexey_karenin = occurrences_2('alexey karenin') + occurrences_2('alexey alexandrovitch')
    main_chars['Alexey Karenin'] = alexey_karenin

    konstantin_levin = occurrences_2('konstantin') + occurrences_2('levin') + occurrences_2('kostya') - \
                       occurrences_2('konstantin levin')
    main_chars['Konstantin Levin'] = konstantin_levin

    all_parts['Part ' + str(name)] = main_chars


character_count(ak_p1_lem, 1)
character_count(ak_p2_lem, 2)
character_count(ak_p3_lem, 3)
character_count(ak_p4_lem, 4)
character_count(ak_p5_lem, 5)
character_count(ak_p6_lem, 6)
character_count(ak_p7_lem, 7)
character_count(ak_p8_lem, 8)

print(all_parts)

# barplotting
# keys = all_parts.keys()
# values = all_parts.values()
#
# plt.xticks(rotation=45)
# plt.savefig('main_characters_complete.png', dpi=400, bbox_inches='tight')

df = pd.DataFrame(all_parts)
df.plot(kind='bar', stacked=True)

plt.show()
plt.savefig('global_count.png', dpi=400, bbox_inches='tight')

# import seaborn as sns
#
# sns.barplot(df)