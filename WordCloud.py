from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import pyperclip
import sys

text = pyperclip.paste()
w = int(sys.argv[1])
h = int(sys.argv[2])
bgc = sys.argv[3]
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width = w, height = h,
                background_color =bgc,
                stopwords = stopwords,
                min_font_size = 10).generate(text)

# plot the WordCloud image
plt.figure(figsize = (w//100, h//100), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
