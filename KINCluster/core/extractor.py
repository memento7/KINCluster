from core.item import Item
from lib.tokenizer import stemize
from lib.stopwords import stopwords
import settings

from typing import List, Union, Any
from math import log10 as normalize
from collections import Counter
from itertools import chain
from functools import reduce
import re

# type hinting
itemID = int # item id
dID = int # document id
wID = str # word id, it str cuz word counter, {word: count}

import numpy as np

class extractable:
    s = {}
    def __init__(self, func):
        extractable.s[func.__name__] = func
        self.func = func
    def __get__(self, obj, klass=None):
        def _call_(*args, **kwargs):
            return self.func(obj, *args, **kwargs)
        return _call_

class Extractor:
    def __init__(self, cluster, tokenizer=stemize, notword='[^a-zA-Z가-힣0-9]'):
        self.tokenizer = tokenizer
        self.not_word = re.compile(notword)
        self.__c = cluster
        self._words = Counter()
        for word, obj in self.__c.vocab.items():
            self._words[word] = obj.count

    @staticmethod
    def __find_center(vectors: np.ndarray) -> int:
        if isinstance(vectors, list):
            h = len(vectors)
            w = len(list(chain.from_iterable(vectors))) / h
        else:
            h, w = vectors.shape
        mean = np.mean(vectors)
        return mean, int(np.abs(vectors - mean).argmin() / w)

    def __get_word_count(self, items: List[Item]) -> Union[set, List[Counter]]:
        counter = Counter()
        for idx, item in enumerate(items):
            for word in self.tokenizer(repr(item)):
                if not word in stopwords() and not self.not_word.search(word):
                    counter[word] += 1
        return counter

    def dump(self, iid: itemID) -> Item:
        return Item(**{e: f(self, iid) for e, f in extractable.s.items()})

    @extractable
    def topic(self, iid: itemID) -> int:
        """topic
        """
        items, vectors = map(list, zip(*self.__c.dumps[iid]))
        _, index = Extractor.__find_center(vectors)
        return index

    @extractable
    def keywords(self, iid: itemID, top: int = 32) -> List[str]:
        """keywords
        """
        items, vectors = map(list, zip(*self.__c.dumps[iid]))
        mean, index = Extractor.__find_center(vectors)
        counter = self.__c.vocab_count[iid]

        def _get_f(t: wID) -> float:
            return float(counter[t])
        def _get_tf(t: wID) -> float:
            max_f = max([_get_f(w) for w in counter.keys() ])
            return .5 + (.5 * _get_f(t) / max_f)
        def _get_idf(t: wID) -> float:
            return 0.01 + normalize(len(self.__c.items)/len(self.__c.dumps[iid]))
        def _get_score(t: wID) -> float:
            return _get_tf(t) * _get_idf(t) + _get_f(t) * 0.001

        words = [(w, _get_score(w)) for w in counter.keys()]
        return sorted(words, key=lambda w: -float(w[1]))[:top]

    @extractable
    def quotation(self, iid: itemID) -> List[str]:
        """quotation
        """
        pass