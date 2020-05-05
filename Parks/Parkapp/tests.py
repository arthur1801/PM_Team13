from django.test import TestCase
from .models import Profile , Parkimg ,B7data
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test', email='test@test.com', password='top_secret')

    def test(self):
        user_test = User.objects.get(username='test')
        p = Profile.objects.get(user=user_test)
        self.assertEqual(user_test,p.user)



class ParkimgTestCase(TestCase):
    def setUp(self):
        park = B7data.objects.create(Name='park')

    def test(self):
        park_test = B7data.objects.get(Name='park')
        p = Parkimg.objects.create(park=park_test)
        self.assertEqual(park_test,p.park)


class B7dataTestCase(TestCase):
    def setUp(self):
        park = B7data.objects.create(Name='park')

    def test(self):
        park_test = B7data.objects.get(Name='park')
        self.assertEqual(park_test.Name,'park')