import unittest
from app import db
from app.models import Comment, User, Pitch

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_wilsonz = User(username = 'wilsonz', password = 'potato', email = 'wilsonz@ms.com')
        self.new_pitch = Pitch(id = 1, pitch_title = 'Test', pitch_content = 'This is a test pitch', category = 'interview', user = self.user_wilsonz)
        self.new_comment = Comment(id = 1, comment = 'Test comment', user = self.user_wilsonz, pitch_id = self.new_pitch)
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_wilsonz)
        self.assertEquals(self.new_comment.pitch_id,self.new_pitch)
