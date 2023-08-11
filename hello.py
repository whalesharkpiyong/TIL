import certifi
ca = certifi.where()

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@whaleshark.owaswsv.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

doc = {
    'name':'영수',
    'age':24
}


# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
db.users.insert_one({'name':'영희','age':30})
db.users.insert_one({'name':'철수','age':20})
db.users.insert_one({'name':'john','age':30})


# 모든 데이터 뽑아보기
all_users = list(db.users.find({},{'_id':False}))
print(all_users[0])         # 0번째 결과값을 보기
print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기


for a in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(a)
    break

user = db.users.find_one({})
print(user)

