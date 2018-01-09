import abc
import re
import pickle
import os
import copy
from datetime import datetime  as dt
from collections.abc import Sequence

class AbstractDataStore(Sequence,metaclass=abc.ABCMeta):
    
    def __init__(self):
        self.words = {}     

    def __iter__(self):
        return iter(self.words)
    
    def __len__(self):
        return len(self.words)

    def __getitem__(self,word_name):
        return self.select(word_name)

    @abc.abstractmethod
    def load(self,src):
        pass

    @abc.abstractmethod
    def save(self,dst):
        pass

    @abc.abstractmethod
    def add(self,data):
        pass

    @abc.abstractmethod
    def select(self,data):
        pass

    @abc.abstractmethod
    def update(self,data):
        pass

    @abc.abstractmethod
    def delete(self,word):
        pass

class PcklDataStore(AbstractDataStore): 

    def load(self,src='default.pkl' ):
        if os.path.isfile(src):
            with open(src,mode="rb") as f :
                while 1:
                    try:
                        # data = pickle.load(f)
                        # self.words[data.word_name] = data 
                        self.words = pickle.load(f)
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
        #         data = WordData(mt.group(1),None,mt.group(2))
        #         self.dict.append(data)
        # [ print(x.word) for x in self.dict ]

    def save(self,dst='default.pkl'):
        with open(dst, mode="wb") as f:
            pickle.dump(self.words, f)
        return True

    def select(self,word_name):
        if ( word_name in self.words):
            return self.words[word_name] 
        else :
            return None

    def update(self,data):
        if ( data.word_name in self.words):
            self.words[data.word_name] = data
            return True
        else:
            return False

    def add(self,data):
        # self.words[data.word_name] = copy.copy(data)
        self.words[data.word_name] = data
        return True

    def delete(self,word_name):
        if ( word_name in self.words):
            del self.words[word_name]
            return True
        else :
            return False

class WordData(object):
    def __init__(self,word_name, type=None, discription=None,example=None,date=dt.now()):
        self.word_name = word_name
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