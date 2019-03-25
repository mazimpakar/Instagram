from django.test import TestCase
from .models import User,Images,Profile
import datetime as dt
# Create your tests here.

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rose= User(first_name = 'rose', last_name ='Mazimpaka', email ='rosemazimpaka2@gmail.com')

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,User))

    # Testing Save Method
    def test_save_method(self):
        self.rose.save_user()
        usere = User.objects.all()
        self.assertTrue(len(user) > 0)
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.rose= User(first_name = 'rose', last_name ='Mazimpaka', email ='rosemazimpaka2@gmail.com')
        self.rose.save_editor()

        # Creating a new tag and saving it
        self.new_profile = profiles(name = 'testing')
        self.new_profile.save()                        

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',user = self.rose)
        self.new_image.save()

        self.new_image.profile.add(self.new_profile)

    def tearDown(self):
        User.objects.all().delete()  
        profiles.objects.all().delete()
        image.objects.all().delete()

    # def test_get_news_today(self):
    #     today_news = Article.todays_news()
    #     self.assertTrue(len(today_news)>0)
    
    # def test_get_news_by_date(self):    
    #     test_date = '2017-03-17'
    #     date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    #     news_by_date = Article.days_news(date)
    #     self.assertTrue(len(news_by_date) == 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# Create your tests here.
