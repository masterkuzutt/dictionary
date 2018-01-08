import abc
import re
import pickle
from datetime import datetime  as dt

class AbstractDataStore(metaclass=abc.ABCMeta):
    
    def __init__(self):
        self.dict = []     

    def __iter__(self):
        return iter(self.dict)

    @abc.abstractmethod
    def load(self,src):
        pass

    @abc.abstractmethod
    def save(self,dst):
        pass

    @abc.abstractmethod
    def insert(self,data):
        pass

    @abc.abstractmethod
    def update(self,data):
        pass

    @abc.abstractmethod
    def delete(self,word):
        pass

class PcklDataStore(AbstractDataStore): 

    def load(self,src='default.pkl' ):
        with open(src,mode="rb+") as f :
            while 1:
                try:
                    self.dict.append( pickle.load(f))
                except EOFError:
                    break
        return True

    def convert_from_csv(self,src):
        pass
        # [TODO] this section is for import text file. it should be removed
        # pt = re.compile(r"^([a-zA-Z\s\-]+),(.*)$")
        # with open ( filepath, "r") as f:
        #     for li in f:
        #         mt = re.match(pt, li.rstrip())
        #         data = DictData(mt.group(1),None,mt.group(2))
        #         self.dict.append(data)
        # [ print(x.word) for x in self.dict ]

    def save(self,dst='default.pkl'):
        with open(dst, mode="wb") as f:
            for data in self.dict:
                pickle.dump(data, f)

    def update(self,word,data):
        pass

    def insert(self,data):
        self.dict.append(data)

    def delete(self,word):
        for index,data in enumerate(self):
            if data.word == word:
                self.dict.pop(index)



class DictData(object):
    def __init__(self,word, type=None, discription=None,example=None,date=dt.now()):
        self.word = word
        self.type = type
        self.discription = discription
        self.example = example
        self.date = date
        self.last_update = date

def main():
    
    test = PcklDataStore()
    test.insert()
    test.update()
    test.delete()
    
    

if __name__ == '__main__':
    main()