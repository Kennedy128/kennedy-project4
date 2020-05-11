from app.models import Comment,User,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
  def setUp(self):
    self.user_victor = User(username = 'kennedy',password = '0711468410', email = 'kennedymbithi12@gmail.com')
    self.new_blog = Pitch(id=1,title='Test',content='This is a test pitch',user = self.user_kennedy)
    self.new_comment = Comment(id=1, content='Test comment',user=self.user_kennedy,blog=self.new_blog)


  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.content,'Test comment')
    self.assertEquals(self.new_comment.user,self.user_victor)
    self.assertEquals(self.new_comment.blog,self.new_blog)