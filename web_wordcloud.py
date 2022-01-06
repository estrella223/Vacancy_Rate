from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

text = open('web_crawling20_2분기.txt', encoding='UTF8').read()

mask = np.array(Image.open('house.png'))
stopwords = set(STOPWORDS)
# stopwords.add("공실률")
# stopwords.add("오피스")
# stopwords.add('상가')
# stopwords.add('상권')
# stopwords.add('공실')
# stopwords.add('1분기')
# stopwords.add('2분기')
# stopwords.add('3분기')
# stopwords.add('코로나')
# stopwords.add('확진자')
# stopwords.add("대유행에")
# stopwords.add('코로나19')
# stopwords.add("3차 대유행")
# stopwords.add('3차')
# stopwords.add("대유행'")

wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", max_words=1000, mask=mask, stopwords=stopwords,
               margin=5, random_state=1).generate(text)
              # margin은 여백
              # if random object is given, this ti used for generating random numbers
default_colors = wc.to_array()    # convert to array for recoloring

import random
def web_color_func(word, font_size, position, orientation,
                    random_state = None, **kwargs):
    return 'hsl(200, 100%%, %d%%)' % random.randint(60, 100)
          # hsl(색상, 채도, 명도)
          # 색상 0=red, 120=green, 240=blue. 0~360까지 가능
          # 채도 0%는 회색, 100%는 풀걸러
          # 명도 0%는 블랙, 100%는 화이트

plt.figure(figsize=(12, 12))
plt.imshow(wc.recolor(color_func=web_color_func, random_state=3),
           interpolation='bilinear')
plt.axis('off')
plt.show()