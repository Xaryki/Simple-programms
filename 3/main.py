import string
import operator
from collections import Counter
import copy
import re
letter_small = string.ascii_lowercase
letter_big = string.ascii_uppercase


def top_3_words(text):
    reg = re.compile('[^a-zA-Z ]')
    text2 = reg.sub('', text)
    if text2.replace(' ','').isalpha() == False:
        return []
    else:
        pass
    text=str.lower(text)
    list = []
    answer = fuck_you(text)
    count = Counter(answer)
    for letter_top in count.most_common(3):
        list.append(letter_top[0])
    return list


def fuck_you(text):
    word = ""
    list = []
    if type(text) == str:
        text+=" "
        for letter in text:
            if (letter in letter_small or letter in letter_big) or (letter == "'"):
                if letter =="'":
                    for letter2 in text:
                        if letter2 =="'":
                            pass
                        else:
                            word+=letter
                        break
                else:
                    word += letter
            else:
                if word != "":
                    list.append(word)
                    word = ""
    return list




if __name__ == '__main__':
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))

