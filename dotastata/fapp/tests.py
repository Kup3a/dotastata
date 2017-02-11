from django.test import TestCase

# Create your tests here.

class MyTest(TestCase):
    def test_ok(self):
        a = 1

    def test_bad(self):
        a = 1 / 0

