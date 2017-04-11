from konlpy.tag import Mecab
import settings

from typing import List, Union
from itertools import chain
import re


# type hinting
TAG = str

tagger = Mecab()

stop_words = settings.STOP_WORDS
pos_tag = settings.TOKEN_POS_TAG
neg_tag = settings.TOKEN_NEG_TAG
zip_tag = settings.TOKEN_ZIP_TAG
zip_token = "**//*///**/*//*//*"
def tokenizer_init():
    # stop_words = []
    # pos_tag = []
    # neg_tag = []
    # zip_tag = [[]]
    # zip_token = ""
    pass

def filter_stopwords(text) -> str:
    return " ".join([t for t in text.split() if not t in settings.STOP_WORDS])

def filter_tag(text, pos_tag : List[TAG] = pos_tag, neg_tag : List[TAG] = neg_tag) -> str:
    # negative filter
    if not pos_tag:
        return " ".join([w for w, t in tagging(text) if not t in neg_tag])
    # positive fileter
    else:
        return " ".join([w for w, t in tagging(text) if t in pos_tag])

# find quotation for 'important word'
pat_small_quot = re.compile(u"\'(.+?)\'")
pat_double_quot = re.compile(u"\"(.+?)\"")
def find_quotations(text):
    mat_small = pat_small_quot.finditer(text)
    mat_double = pat_double_quot.finditer(text)
    return list(mat_small) + list(mat_double)

def tokenize(text) -> List[str]:
    return text.split()

def stemize(text, pos_tag : List[TAG] = pos_tag, neg_tag : List[TAG] = neg_tag) -> List[str]:
    # (extracted words, extracted text)
    def extract_quotations(text) -> Union[List[str], str]:
        matches = []
        c = 0
        for match in find_quotations(text):
            text = " ".join([text[:match.start() + c], zip_token, text[match.end() + c:]])
            c += len(zip_token) - len(match.group()) + 2
            matches.append(match.group()[1:-1])
        return (matches, text)

    def zip_tokens(tokens):
        for zip_pat in zip_tag:
            if tokens[0][1] in zip_pat and tokens[-1][1] in zip_pat:
                words, tokens = map(list, zip(*tokens))
                tokens = [("".join(words), 'ZIP')]
        for word in list(zip(*tokens))[0]:
            yield word
        
    matches, text = extract_quotations(text)
    words = [zip_tokens(tokens) for tokens in [tagger.pos(word) for word in text.split()]]
    ret = list(chain.from_iterable(words))
    return [r == zip_token and matches.pop() or r for r in ret]

def tagging(text) -> List[Union[str, TAG]]:
    return tagger.pos(text)

tokenizer_init()