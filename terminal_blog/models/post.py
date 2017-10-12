import uuid
from database import Database
import datetime

class Post(object):
    def __init__(self,blog_id, title, content, authorName, date=datetime.datetime.utcnow(), id=None): #like constructor  -for id field, if no value passed, it takes None
        self.title = title
        self.content = content
        self.author = authorName
        self.blog_id=blog_id
        self.id = "10-12-2017" if id is None else id  #if id is none take random id else take id from args
        self.created_date = date

    def save_to_mongo(self):
        Database.insert(collection='post', data=self.json())

    def json(self):
        return {
            'id':self.blog_id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.content,
            'created_date':self.created_date
        }
    @staticmethod
    def from_mongo(id):
        # to get posts with id number
        return Database.find_one(collection='post', query={'id':id})

    @staticmethod
    def from_blog(id):
        # Database.find(collection='posts', query={'blog_id':id})  -- will return pymongo cursor
        # so we need below stmts, to returning a list of posts
        return [post for post in Database.find(collection='post', data={'blog_id':id})]

