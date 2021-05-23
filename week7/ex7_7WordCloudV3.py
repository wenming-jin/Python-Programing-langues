#Author:WenmingJin
#CreateTime:2021/5/23
#FileName:ex7-7WordCloudV3
#Discription:
import jieba
import wordcloud
from imageio import imread
mask = imread("chinamap.jpg")
excludes = { }
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask,max_words=15
    )
w.generate(txt)
w.to_file("grwordcloudm.png")