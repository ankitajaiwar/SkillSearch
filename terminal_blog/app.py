import pymongo
from database import Database
from models.blog import Blog
from models.post import Post

Database.initialize()

blog = Blog(author="Vignesh Blog",
            title="Sample title",
            description="here goes the description of nothing.")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.get_from_mongo(blog.id)

print(blog.get_posts())








# Get content from Mongo
# p1 = Post.from_mongo("123")
# p2 = Post.from_blog("1213")     #Note - This is a static method of Post
# print(p1)
# print(p2)

# To insert content into DB
# post = Post(title="Master of One",
#             content="Be a jack of all trades and Master of one",
#             blog_id="1213",
#             authorName="Vic",
#             id="2")
#
# post.save_to_mongo()

