import unittest
import os 
from unittest import TestCase
from app.datastore import PcklDataStore,WordData

class TestPcklDataStore(TestCase):
    def setUpClass():
        pass

    def setUp(self):
        self.pkds = PcklDataStore()

    def tearDown(self):
        if os.path.isfile('default.pkl'):
            os.remove('default.pkl')

    def tearDownClass():
        pass

    def test_init(self):
        self.assertEqual(len(self.pkds),0)

    def test_add(self):
        self.pkds.load()
        data = WordData("test") 
        self.assertTrue(self.pkds.add(data))
        self.assertEqual(self.pkds[data.word_name],data)

    def test_save(self):
        self.pkds.load()
        data = WordData("test") 
        self.pkds.add(data)
        self.assertTrue(self.pkds.save())

    def test_load(self):
        self.pkds.load()
        self.assertEqual(len(self.pkds),0)

        data1 = WordData("test1") 
        self.pkds.add(data1)
        self.pkds.save()
        self.pkds.load()
        self.assertEqual(len(self.pkds),1)

        data2 = WordData("test2") 
        self.pkds.add(data2)        
        self.pkds.save()
        self.pkds.load()
        self.assertEqual(len(self.pkds),2)

    def test_update(self):  
        self.pkds.load()
        data = WordData("test") 
        self.pkds.add(data)
        self.pkds.save()
        self.pkds.load()

        data = self.pkds.select("test")
        data.discription = "test discription"
        self.pkds.update(data)        
        self.pkds.save()
        
        self.pkds.load()
        data = self.pkds.select("test")
        self.assertEqual(data.discription,"test discription")  


    def test_delete(self):  
        self.pkds.load()
        data = WordData("test") 
        self.pkds.add(data)
        self.pkds.save()
        self.pkds.load()

        self.pkds.delete("test")
        self.pkds.save()
        
        self.pkds.load()
        data = self.pkds.select("test")
        self.assertEqual(data,None)  


# def main():
#     unittest.main()

# if __name__ == '__main__':
#     main()