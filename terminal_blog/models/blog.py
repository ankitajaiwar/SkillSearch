import uuid

import datetime

from database import Database
from models.post import Post

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter title for blog")
        content = input("Enter content for new blog")
        date = input("Enter date DDMMYY or leave blank")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    authorName=self.author,
                    date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    @staticmethod
    def get_from_mongo(id):
        blog_data = Database.find_one(collection="blogs",
                                      query={'id':id})
        return Blog(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['id'])
    #In the above method, we are returning data values. Moreover, if we change class name of Blog,
    # we have to update here as well. Instead we can change the implementation to return an object,
    # Like shown commentted section below:

    # @classmethod
    # def get_from_mongo(cls,id):
    #     blog_data = Database.find_one(collection="blogs",
    #                                   query={'id':id})
    #     return cls(author=blog_data['author'],
    #                 title=blog_data['title'],
    #                 description=blog_data['description'],
    #                 id=blog_data['id'])

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description':self.description,
            'id':self.id
        }

