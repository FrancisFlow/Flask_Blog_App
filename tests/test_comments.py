import unittest
from app.models import Blog, User
from app import db
from flask_login import current_user


class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.user_francis=User(username='francis', password='francis2022', email='francisngigi948@gmail.com')
        self.new_blog=Blog(id=1, title='Theone', content='From the high valleys and low mountains, his spirit would not yield', user_id=self.user_francis.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Theone')
        self.assertEquals(self.new_blog.content, 'From the high valleys and the low mountains, his spirit would not yield')
        self.assertEquals(self.new_blog.user_id, self.user_francis.id)
    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)
    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        the_blog = Blog.get_blot(1)
        self.assertTrue(len(the_blog)==1)