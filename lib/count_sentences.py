#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
           self._value = value
        else:
            print("The value must be a string.")


    def is_sentence(self):
          if self.value.endswith("."):
              return True
          else:
              return False
    
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else: 
            return False   
 
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False
        
    def count_sentences(self): 
        sentence = re.split(r'\s*[.?!]\s*', self.value)
        """ sentence= str.replace(string, sentence) """
        sentence = [s for s in sentence if s]
        count = len(sentence)
        return count


string = MyString()
string.value = "This is a string! It has three sentences. Right?" 
#string.count_sentences("This is a string! It has three sentences. Right?")       