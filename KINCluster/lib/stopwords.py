
import settings 

from itertools import chain
from os import listdir
from os.path import join, dirname, abspath

def stopwords():
    path = abspath(__file__)
    stopwords_dir = join(dirname(__file__), 'stopwords')
    words = set()
    for file_name in listdir(stopwords_dir):
        for word in open(join(stopwords_dir, file_name)).readlines():
            words.add(word)
    return map(lambda x: x.strip(), words)