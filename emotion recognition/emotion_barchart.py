import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # for percentage in barchart

# read results of emotion recognition to dataframes
df1 = pd.read_csv('p1.csv', index_col=0)
df2 = pd.read_csv('p2.csv', index_col=0)
df3 = pd.read_csv('p3.csv', index_col=0)
df4 = pd.read_csv('p4.csv', index_col=0)
df5 = pd.read_csv('p5.csv', index_col=0)
df6 = pd.read_csv('p6.csv', index_col=0)
df7 = pd.read_csv('p7.csv', index_col=0)
df8 = pd.read_csv('p8.csv', index_col=0)

# reformat values to fit into barchart

emotions = {'anger': {}, 'joy': {}, 'sadness': {}, 'fear': {}, 'love': {}}


def reformat(file, fname):
    anger = file['Emotion'].value_counts(normalize=True)['anger'] * 100
    joy = file['Emotion'].value_counts(normalize=True)['joy'] * 100
    sadness = file['Emotion'].value_counts(normalize=True)['sadness'] * 100
    fear = file['Emotion'].value_counts(normalize=True)['fear'] * 100
    love = file['Emotion'].value_counts(normalize=True)['love'] * 100

    emotions['anger']['Part ' + str(fname)] = anger
    emotions['joy']['Part ' + str(fname)] = joy
    emotions['sadness']['Part ' + str(fname)] = sadness
    emotions['fear']['Part ' + str(fname)] = fear
    emotions['love']['Part ' + str(fname)] = love


reformat(df1, 1)
reformat(df2, 2)
reformat(df3, 3)
reformat(df4, 4)
reformat(df5, 5)
reformat(df6, 6)
reformat(df7, 7)
reformat(df8, 8)


# create barchart

df_chart = pd.DataFrame(emotions)
plot_emotions = df_chart.plot(kind='bar', stacked=True, legend='reverse')
plot_emotions.legend(loc='center left', bbox_to_anchor=(1, 0.5))    # legend out of plot
plot_emotions.yaxis.set_major_formatter(mtick.PercentFormatter())   # percentage in y-label
plt.savefig('emotions.png', dpi=400, bbox_inches='tight')
