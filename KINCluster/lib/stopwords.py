import codecs
from os import listdir
from os.path import join, dirname

def __get_stopwords():
    stopwords_dir = join(dirname(__file__), 'stopwords')
    words = set()
    for file_name in listdir(stopwords_dir):
        for word in codecs.open(join(stopwords_dir, file_name), "r", "utf-8").readlines():
            words.add(word)
    return map(lambda x: x.strip(), words)
stopwords = list(__get_stopwords())
