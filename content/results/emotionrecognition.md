---
title: "Emotion Recognition"
date: 2022-09-05T01:02:25+02:00
draft: false
weight: 5
---

Finally, as a more advanced method of analysis, an emotion recognition algorithm was written to explore the emotions in more detail (based on [this article](https://medium.com/analytics-vidhya/song-recommendation-based-on-textual-and-facial-emotion-recognition-a95e6259c5d8) by Abhinav Kumar). After training a machine learning model, each sentence of the book is classified with either anger, joy, sadness, surprise, fear, or love:

To achieve this, the machine learning model first has to be trained on a dataset, which assigns one of the six emotions noted above to a large number of sentences. After training the model, the book text is loaded and tokenized into individual sentences, as well as divided into the eight parts of the book. These sentences are then analyzed by the model and the results visualized into a bar plot showing the percentage of emotions throughout all sentences of one book part.

![Emotions](/img/emotions.png)

Looking at the results, one can see a large percentage of sentences that are assigned the emotion "anger". If one then looks at the corresponding individual assigned emotions, it becomes obvious that many sentences are classified with "anger" that are almost not emotionally charged at all. This unfortunate "noise" in the data is due to the [dataset](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp) that was used for training the model. Unfortunately, there not many other high-quality public datasets with sufficient data to train a machine learning model on recognizing emotions from sentences.

Despite these obstacles, there are several observations that can be made from the visualization above: First, the size of "sadness" in Part 5: this part of the story is infused with insecurities from many of the major characters who are all trying to figure out their future life. This might explain the rather large bar for "sadness".

A similar observation can be made in Part 3, which is mostly about Levin on his estate, contemplating his future. This part seems to feature slightly less anger than the other parts and slightly more joy, which seems in line with a subjective reading of this part.