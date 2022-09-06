---
title: "Sentiment Analysis"
date: 2022-09-05T01:02:16+02:00
draft: false
weight: 4
---

For this part, the individual sentences of the text are being classified as either negative, neutral or positive by a Sentiment Intensity Analyzer.

As individual graphs, the results look very similar. Only in comparison, e.g. switching rapidly between the different images, one can see subtle difference between the different parts of the book. The used Python module is, however, mostly suited for short and easy texts like Twitter posts or online reviews. The hypothesis made previously that Tolstoy might have wanted to end his novel on a good note would be disputed with the results of this sentiment analysis, as Part 7, where Anna Karenina experiences her mental decline and eventually decides on her suicide, would be more positive and less negative than the epilogue Part 8. Although the final part features by no means a typical happy ending, this result would seem odd given previous results from other analyses. 

In the future, I'd like to retry a sentiment analysis using a more sophisticated method. For now, if one wants to rapidly switch between the different images to see subtle differences, it is advisable to download the respective folder from the [GitHub repository](https://github.com/mansutt/annakarenina/tree/main/sentiment%20analysis/nltk-sia).

![All parts](/img/comp_sent.png)

![Part 1](/img/p1_sent.png)

![Part 2](/img/p2_sent.png)

![Part 3](/img/p3_sent.png)

![Part 4](/img/p4_sent.png)

![Part 5](/img/p5_sent.png)

![Part 6](/img/p6_sent.png)

![Part 7](/img/p7_sent.png)

![Part 8](/img/p8_sent.png)