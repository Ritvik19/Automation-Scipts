from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import pyperclip
import sys

text = pyperclip.paste()
w = int(sys.argv[1])
h = int(sys.argv[2])
bgc = sys.argv[3]
if len(sys.argv) == 5:
    mw = int(sys.argv[4])
else:
    mw = 200
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width = w, height = h,
                background_color =bgc,
                stopwords = stopwords,
                min_font_size = 10,
                max_words = mw).generate(text)

# plot the WordCloud image
plt.figure(figsize = (w//100, h//100), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
