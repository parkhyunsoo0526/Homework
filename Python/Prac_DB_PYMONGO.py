

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title': '월-E'})
star = movie['star']
print(star)

db.movies.update_many({'star': star}, {'$set': {'star': 0}})