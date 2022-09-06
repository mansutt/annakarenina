---
title: "Wordcloud"
date: 2022-09-05T01:02:00+02:00
draft: false
weight: 1
---


Using the Python module [_WordCloud_](https://amueller.github.io/word_cloud/) by Andreas Mueller, a word cloud is built for both the text in and of itself as well as the text in its lemmatized form. The more often a word appears in the given text, the larger the word is displayed in the word cloud. The word cloud excludes predefined stopwords (a full list can be found in [stopwords.txt in the GitHub repository](https://github.com/mansutt/annakarenina/blob/main/wordcl/stopwords.txt), that would add no value to the result. Additionally, words that are commonly used together in the text such as many of the Russian names (e.g. "Stepan Arkadyevitch") are counted as one expression (i.e. counting the occurrences of "Stepan Arkadyevitch" and not "Stepan" and "Arkadyevitch" separately).

![Word Cloud All Parts](/img/ak_complete.png)

If we first take a look at the word cloud of the entire book with the text in its unlemmatized (i.e. "normal") form, several observations can be made. First of all, with "said" being the largest word in the wordcloud, that is merely a representation of the narrative style of the book, which - besides extensive dialogue - features a narrator.

Next, what seems striking is the size of "levin". Since the story centers around its eponymous character of Anna Karenina, it could seem strange at first that Konstantin Levin would be the most frequently named character. This could be due to a multitude of reasons: Firstly, the frequent naming of Levin could be caused by the writing of the character itself. One hypothesis could be, for example, that Levin has less dialogue compared to the other main characters, but is described more often by the narrator. Secondly, it could also be the case that Levin is mentioned so often for the reason that he is generally considered Tolstoy's alter ego representing his political ideas and ideals. If one follows such a hypothesis, this could imply that Tolstoy used Levin's character most frequently in order to comment on the events in the plot and place them into his own worldview. 

![Word Cloud All Parts, Lemmatized](/img/ak_complete_lem.png)

Looking at the word cloud with the entire text in its lemmatized form, we see several patterns. "Say" is still the largest word, but we now have several other verbs in their basic form that also take up a large space. This is probably due to the fact, that "say" is almost exclusively used with a narrative "said", while verbs like "see", "come", "know", "think", etc. are used for all kinds of purposes in several conjugated forms. Lemmatizing the text merges all these forms into just their basic form, which causes the many different verbs that were much smaller (or not there at all) in the first word cloud.

Other than that there are not many notable differences between the two word clouds.

---

Further down are the word clouds for each of the eight parts of the book in their unlemmatized and lemmatized form respectively.  

### Part One

![Word Cloud Part 1](/img/ak_p1.png)

![Word Cloud Part 1, Lemmatized](/img/ak_p1_lem.png)

In this case, once again, we can see the benefit of using lemmatization in the word "go". In the word cloud of the unlemmatized text, we can see the words "go" and "went" appear relatively small on the left and upper left respectively, while in the lemmatized text, it is one of the largest words. 

This part, like the book in its entirety, features Levin most frequently of the characters.

Another observation that can be made from this part of the book: While "go" is a widely used verb, it does not appear equally as often in the different parts of the book, as we can see in the different word clouds, which could be a basis for hypotheses.

### Part Two

![Word Cloud Part 2](/img/ak_p2.png)

![Word Cloud Part 2, Lemmatized](/img/ak_p2_lem.png)

As we can see, the second part of the book features mostly Vronsky and Kitty. This is in line with the plot which, in this part, features Kitty's and Vronsky's mostly individual stories as Kitty is recovering from her failing health and Vronsky takes on a horseriding event.

One observation that can be made, especially from the lemmatized word cloud is the relatively large size of the word "know", which appears much more frequently in this part than in most others. Whether this implies certainty (e.g. "I know") or more uncertainty (e.g. "I don't know") is not evident but could be an interesting subject for further investigation.

### Part Three

![Word Cloud Part 3](/img/ak_p3.png)

![Word Cloud Part 3, Lemmatized](/img/ak_p3_lem.png)

Part 3 once again features Konstantin Levin the most, which is not surprising, considering this part is mostly about Levin's life on his estate. One observation that might be of interest, is the relative size of "would" and "could". One could speculate that this is due to the fact that Levin spends a lot of time in this chapter reflecting on his life and on aspirations for the future, although this conclusion would require a more systematic investigation.

### Part Four

![Word Cloud Part 4](/img/ak_p4.png)

![Word Cloud Part 4, Lemmatized](/img/ak_p4_lem.png)

One thing that immediately springs to mind about the word cloud of Part 4 is the absence of few but large words. Instead, one can see a broader distribution of words. The only notable large-sized word (or name in this instance) that one can see in both the normal and the lemmatized word cloud is "alexey alexandrovitch" which, again, is unsurprising, as Part 4 heavily features Alexey Karenin thinking about and consulting a lawyer about a possible divorce from his wife, Anna Karenina.

Nonetheless, the diverse array of words without any particularly prominent words beside "say" and "alexey alexandrovitch" looks interesting and invites for speculation. Once again, though, a thorough investigation from literary scholars would be needed.

### Part Five

![Word Cloud Part 5](/img/ak_p5.png)

![Word Cloud Part 5, Lemmatized](/img/ak_p5_lem.png)

In contrast, the word cloud for Part 5 looks very different. There are several words of prominent size. Especially the differences between the normal and lemmatized word clouds are striking. While Levin is featured particularly often in the normal word cloud, his name shrinks considerably in the lemmatized word cloud and instead gives room for verbs like "come", "see" and "go".

Another interesting observation can be made in the first word cloud, as the words "could" and "would" are particularly prominent. As in Part 3, the speculation can be made that this is due to the fact that this part sees many characters in changing life situations. Levin and Kitty get married and get used to their new life on Levin's estate, struggling with their different ideas for the future as a married couple. Meanwhile, Anna Karenina and Vronsky are spending time alone (away from Anna's still-husband) and are themselves pondering possibities for their future together while being concerned about Anna's position in society. Especially this last concern, one might speculate, could be the reason for the size of the word "see" in the lemmatized word cloud, as Anna often thinks about how she is being seen by society (figuratively as well as literally while visiting a theatre performance in St. Petersburg).

### Part Six

![Word Cloud Part 6](/img/ak_p6.png)

![Word Cloud Part 6, Lemmatized](/img/ak_p6_lem.png)

Besides still featuring "would" and "could" prominently, the normal world cloud features mostly Levin and Anna. This might be due to Darya Alexandrovna, whose name is also featured relatively prominently, visiting both the Levins as well as Anna and Vronsky at their respective residence. While "levin" remains a rather large word in the lemmatized word cloud, though, "anna" gets overshadowed by verbs such as "go", "see", "know" and "come". More unusual is the size of "well" at the right border of the image, which was not featured as prominently in the previous word clouds.

### Part Seven

![Word Cloud Part 7](/img/ak_p7.png)

![Word Cloud Part 7, Lemmatized](/img/ak_p7_lem.png)

This final part of the main story majorly features Stepan Arkadyevitch and Levin again, who spend some time together mostly at the beginning of Part 7 and then go on to visit people throughout the rest of this part of the book. What seems surprising, however, is how few times "anna" is mentioned according to the size of her name, given that her mental state degrades further and further along the story, ultimately culminating into her suicide. While reading this part of the book, Anna Karenina's mental struggles eventually become the major story line which makes it surprising that very few traces of it can be found on either of the two word clouds.

Another event that is not outright visible on these word clouds is the birth of the Levins' child, also a major event in the plot. This exemplifies some of the limitations of a quantitative analysis of a literary text, which for a thorough investigation should be used as an additional means of analysis, not a replacement of existing ones.

### Part Eight

![Word Cloud Part 8](/img/ak_p8.png)

![Word Cloud Part 8, Lemmatized](/img/ak_p8_lem.png)

This last part and epilogue of the book once again shows a more distributed array of words. The plot of the final part is represented through "sergey ivanovitch", which is the largest word in these word clouds, as he plays a major role at the beginning of this part. 

Among the other prominent words in these word clouds, several plot lines can be seen. For example the medium-sized word "god" (in the center-right) represents Levin's struggles with religion, ultimately no longer rejecting but accepting his Christian faith.

An other interesting observation that can be made in the lemmatized word cloud is the size of the words "live" and "life". One might speculate that this represents all the characters in the final part reflecting on their lives and their ideas of their future. Additionally, several positively connotated words can be seen, such as "smile" and "well", which might represent Tolstoy's intent to end the novel on a positive note. 
