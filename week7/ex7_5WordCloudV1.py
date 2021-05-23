#Author:WenmingJin
#CreateTime:2021/5/23
#FileName:ex7_5WordCloud
#Discription:词云
import wordcloud
c=wordcloud.WordCloud()
c.generate('wordcloud and python and python')
c.to_file('pywordcloud.png')