---
title: "Count"
date: 2022-09-05T01:02:06+02:00
draft: false
weight: 2
---

As one means of analysis, two counting methods were used and the respective results visualized. While a count of the major characters looks at the number of occurrences of the respective character in total as well as the different parts of the book, a location count looks at the occurrences of the two major plot locations St. Petersburg and Moscow, as well as Konstantin Levin's and Alexey Vronsky's estate.

Using such tools can help in trying to gain a better understanding of the story and its implications. The results offer insights into the composition of the different parts of the book and how the characters and locations are represented in each of them.


### Character Count

The difficulty in counting the characters of the book lies mostly in the Russian names. For example, Stepan Oblonsky's full name is "Stepan Arkadyevitch Oblonsky" while he also has a nickname, "Stiva". Most people call him either "Stepan Arkadyevitch" or "Stiva" but others might also call him by his last name. In this instance, the Python script counts the occurrences of "Stepan Arkadyevitch", "Stiva", and "Oblonsky" and adds the different counts. There will never be a perfect count because people might call him "Stiva Oblonsky" and therefore add two occurrences instead of just one, but I have tried to account for the most common naming schemes (e.g. if someone were to call him "Stepan Oblonsky" it would only count as one since "Stepan" is not counted individually).

One difficulty that arises, however, is two characters being named Alexey - Alexey Vronsky and Alexey Karenin. Given that both of them are regularly addressed as "Alexey" this makes it impossible to count their respective occurrences. This is why the plot features an "Alexey (unclear)", which are all the occurrences of "Alexey" that could not be reliably distinguished. The bar of "Alexey (unclear)" does look very similar to that of Alexey Karenin, however, so one can speculate that most of those occurrences belong to Alexey Karenin.

![Character Count](/img/characters.png)

As can be seen in the image above, Konstantin Levin is by far the most mentioned character, being named about twice as much as the eponymous Anna Karenina. As with the word clouds, this can most likely be explained due to the character being generally considered Lev Tolstoy's alter ego, thereby infusing his own ideas and perspectives into the story.

Levin seems to be featured relatively equally throughout all of the eight parts of the book, with an especially large count in Parts 3 and 6, both of which feature mainly the Levins (only Konstantin Levin in Part 3 plus Kitty in Part 6).


### Location Count

![Location Count](/img/locations.png)

As the plot centers around the locations St. Petersburg and Moscow with their respective countryside, one can see this being visually represented in the plot above. Both major locations are featured in all of the eight parts of the book, although the final part features mostly Moscow and barely mentions St. Petersburg. Given that Tolstoy expresses clear moral judgement about the locations with St. Petersburg being viewed negatively and Moscow being seen as morally superior, one might argue that this could be an attempt by Tolstoy to end the story on a more positive note. What might support this hypothesis is Levin's estate Pokrovskoe being mostly featured in Part 8 (besides Part 3, where Levin spends the entire story on his estate), which for Tolstoy represented the ideal rural life. Additionally, Vozdvizhenskoe, Vronsky's estate, is mostly featured in Part 7, whose storyline features Anna Karenina's declining mental health and ultimately her suicide.
