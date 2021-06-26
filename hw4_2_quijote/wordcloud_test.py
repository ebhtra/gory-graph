import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image  # pillow library


raw = 'This is a bunch of slly words that I like to play with over and over until midnight and then morning.'


# define stop words to be excluded from the word cloud
#stopwords = set(STOPWORDS)
#stopwords.update(["y", "el", "él", "le", "la", "en", "de","ni","o","que","por","lo","su","los","con","se","e","las","del","ya"])
stopwords = [".",",",";",":","—","-","¿","?","¡","!"]

# Using an image define a mask for the word cloud
donquijote_mask = np.array(Image.open("don_quijote_2.png"))

# Generate a word cloud image
wc = WordCloud(stopwords=stopwords, background_color="white",
               max_words=200,
               mask = donquijote_mask,
              contour_width=1,
              contour_color='firebrick').generate(raw)

plt.figure(figsize = (12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
