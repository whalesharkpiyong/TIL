import certifi
ca = certifi.where()

from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://sparta:test@whaleshark.owaswsv.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

URL = "https://movie.daum.net/ranking/boxoffice/yearly?date=2010"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

lis = soup.select(".list_movieranking > li")
for li in lis:
    rank = li.select_one(".rank_num").text
    age = li.select_one(".ico_see").text
    title = li.select_one(".link_txt").text
    print(rank, title, age)
    break

    doc = {
        'rank': rank,
        'title': title,
        'age': age
    }
    break
   
    db.movies2.insert_one(doc)

    # 문제 1. 영화 "아저씨"의 순위 가져오기
    movie = db.movies2.find_one({"title" : "아저씨"})
    print(movie["rank"])
    break

movie = db.movies2.find_one({"title" :"하모니"})
print(movie['age'])

movies = list(db.movies2.find({'age':age},{'_id':False}))
for m in movies:
    print(m['title'])