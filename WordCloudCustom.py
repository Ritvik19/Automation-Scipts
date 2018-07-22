from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import pyperclip
import sys
import numpy as np
from PIL import Image

text = pyperclip.paste()
w = int(sys.argv[1])
h = int(sys.argv[2])
bgc = sys.argv[3]
mw = 200
stopwords = set(STOPWORDS)
i_mask = np.array(Image.open(' '.join(sys.argv[4:])))

wordcloud = WordCloud(width = w, height = h,
                background_color =bgc,
                stopwords = stopwords,
                min_font_size = 10,
                max_words = mw,
                mask = i_mask).generate(text)

# plot the WordCloud image
plt.figure(figsize = (w//100, h//100), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()
