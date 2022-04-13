import sys

# from celestine.tag.alphabet import convert
# from celestine.tag.alphabet import tag
# from celestine.tag.alphabet import hashy
# from celestine.tag.alphabet import space
#from celestine.tag.alphabet import *
sys.path.insert(1, '../')


from celestine.tag.alphabet import convert
from celestine.tag.alphabet import letter
from celestine.tag.alphabet import comparison
from celestine.tag.alphabet import all_token
from celestine.tag.alphabet import one_token
from celestine.unicode.u0000 import LOW_LINE


from celestine.enum import Enum


class State(Enum):
    NONE = 1
    TAG = 2
    HASH = 3
    SPACE = 3
    SYMBOL = 4


# string = input("you ugly")
string = "cat hat"


falcon = []

for character in string:
    falcon.append(convert.get(character, str()))

bird = str().join(falcon)

tigger = []
mouse = []

state_now = State.NONE
state_past = State.NONE






print("START")
print(string)


class translator():
    @staticmethod
    def translate(string):
        return str().join(
            [
                item for item in
                [convert.get(character) for character in string]
                if item is not None
            ]
        )

class tokenizer():
    @staticmethod
    def tokenize(string):
        return string

class parser():
    @staticmethod
    def parse(string):
        return string.split()

string = translator.translate(string)
string = tokenizer.tokenize(string)
string = parser.parse(string)

