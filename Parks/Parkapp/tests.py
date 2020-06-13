from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from .models import Profile , Parkimg ,B7data , Location ,Parent_Childs
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test', email='test@test.com', password='top_secret')

    def test(self):
        user_test = User.objects.get(username='test')
        p = Profile.objects.get(user=user_test)
        self.assertEqual(user_test,p.user)
        self.assertEqual(user_test.email,p.user.email)




class ParkimgTestCase(TestCase):
    def setUp(self):
        park = B7data.objects.create(Name='park')

    def test(self):
        park_test = B7data.objects.get(Name='park')
        p = Parkimg.objects.create(park=park_test)
        self.assertEqual(park_test,p.park)
        self.assertEqual(park_test,p.park)



class B7dataTestCase(TestCase):
    def setUp(self):
        park = B7data.objects.create(Name='park')
        park = B7data.objects.create(Name='park2')

    def test(self):
        park_test = B7data.objects.get(Name='park')
        park_test2 = B7data.objects.get(Name='park2')
        self.assertEqual(park_test.Name,'park')
        self.assertEqual(park_test2.Name,'park2')



class LocationTestCase(TestCase):
    def test(self):
        loc = Location(31.267509,34.789512)
        self.assertEqual(loc.lat,31.267509)
        self.assertEqual(loc.lon,34.789512)




class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Testcase', email='test@gmail.com', password='top_secret1234')

    def test(self):
        user = User.objects.get(username='Testcase')
        self.assertEqual(user.username, 'Testcase')
        self.assertEqual(user.email, 'test@gmail.com')





#---------------integration tests!!!!-------------------------

class ParkimgIntegrationWithParkTestCase(TestCase):
    #test defaul image creating in park
    def setUp(self):
        park = B7data.objects.create(Name='park')

    def test(self):
        park_test = B7data.objects.get(Name='park')
        p = Parkimg.objects.create(park=park_test)
        self.assertEqual(p.image,'default2.jpg')


class ProfileIntegrationWithUSERTestCase(TestCase):
    #test defaul image creating in profile for test user
    def setUp(self):
        user = User.objects.create_user(username='test', email='test@test.com', password='top_secret')

    def test(self):
        user_test = User.objects.get(username='test')
        p = Profile.objects.get(user=user_test)
        self.assertEqual(p.image,'default.jpg')



class ParentKidassignTestCase(TestCase):
    #test kid parent and assigment creation
    def setUp(self):
        Parent = User.objects.create_user(username='test', email='test@test.com', password='top_secret')
        kid = User.objects.create_user(username='test2', email='test2@test.com', password='top_secret')

    def test(self):
        Parent = User.objects.get(username='test')
        kid = Child_Username=User.objects.get(username='test2')
        p_c = Parent_Childs(Parent_Username=Parent,Child_Username=kid)
        self.assertEqual(p_c.Parent_Username.username,'test')
        self.assertEqual(p_c.Child_Username.username,'test2')



class ParkandLocationIntegrationTestCase(TestCase):
    #test kid parent and assigment creation
    def setUp(self):
        park = B7data.objects.create(Name='park',lat=31.267509,lon=34.789512)

    def test(self):
        park_test = B7data.objects.get(Name='park')
        loc = Location(31.267509,34.789512)
        self.assertEqual(park_test.lat,31.267509)
        self.assertEqual(park_test.lon,34.789512)

class RegistrationAndCreatingINDBTestCase(TestCase):
    #test integration of registration form and user creation in DB
    def test(self):
        def test_form(self):
            data = {
                'username': 'testuser',
                'password1': 'test123',
                'password2': 'test123',
            }

            form = UserCreationForm(data)
            user = User.objects.get(username='testuser')
            self.assertEqual(user.username,'testuser')



