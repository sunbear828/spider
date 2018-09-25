#DOUBAN Top 250 movie information
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as urlrequest


url_content='https://movie.douban.com/top250?start={}&filter='
with open('douban250.txt','w',encoding='utf-8',errors='ignore') as file:
    for i in range(0,251,25):
        url=url_content.format(i)
        douban_web=urlrequest.urlopen(url).read()
        http_content =douban_web.decode('utf-8')
        soup=BeautifulSoup(http_content,'html.parser')
        movie_info=soup.find_all(class_='info')
        for movie in movie_info:
            movie_web=movie.find('a')['href']
            movie_title=movie.find('span').get_text()
            movie_character=movie.find('p').get_text().strip('').replace('\n','').replace(u'\u3000', u'').replace(u'\xa0', u'')
            movie_score=movie.find(class_='rating_num').get_text()
            movie_comment=movie.find(class_='inq').get_text()
            file.write('{} {} {} {} {}\n'.format(movie_web,movie_title,movie_character,movie_score,movie_comment))

