import unittest
from unittest import TestCase
from app.datastore import PcklDataStore

class TestPcklDataStore(TestCase):
    def setUp(self):
        self.pkds = PcklDataStore()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.pkds.dict,[])

    def test_iter(self):
        pass  
        #[TODO] learn how to write test case for iterator 

    def test_load(self):
        self.assertTrue(self.pkds.load())

class TestStringMethods(TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello','world'])

        with self.assertRaises(TypeError):
            s.split(2)

# def main():
#     unittest.main()

# if __name__ == '__main__':
#     main()