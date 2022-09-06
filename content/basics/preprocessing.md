---
title: "Preprocessing"
date: 2022-09-05T01:01:41+02:00
draft: false
---

In order to make the text usable for a quantitative analysis, various procedures must first be applied in the context of preprocessing. 

The text was downloaded from Project Gutenberg, since Tolstoy's work itself is no longer subject to copyright. The plain text (.txt) file contains some annotations from Project Gutenberg, as well as a table of contents, which are first removed manually. 

The start of the book then looks like this:

![Text at first](/img/base.png)

Then all lines beginning with "PART" or "Chapter" are deleted from the document to limit the analysis to only relevant content. The text is also divided into the eight parts of the work in order to be able to analyze the book as a whole, as well as the eight parts individually. Next, all blank lines are deleted, punctuation is removed, and all text is converted to lowercase. 

This results in a uniform text without quotation marks, punctuation, capitalization, etc. 
Such a text is no longer particularly pleasant to read for humans, since, e.g. direct speech can no longer be recognized, but it is very helpful for a quantitative analysis. The program code does not recognize words twice (e.g. " House" and "house"), but summarizes all occurrences of a word. 

At this point, the preprocessed text looks like this:

![Preprocessed text](/img/prep.png)

Another problem are the different forms of words (e.g. "be", "are", "am", "family", "families"). If one wants to summarize all forms of words to make a qualified count of the occurrences, these must be lemmatized first. Thereby all words are put back into their respective basic form.

The final version of the text that is suitable for further analysis then looks like this:

![Lemmatized text](/img/lem.png)

All the different version of the text can also be found on the [GitHub repository](https://github.com/mansutt/annakarenina/tree/main/text).