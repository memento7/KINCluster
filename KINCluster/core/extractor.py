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

    def get_topic(self, id: itemID, keyword: str) -> int:
        items, vectors = map(list, zip(*self.__c.dumps[id]))
        filtered = list(filter(lambda iv: keyword in repr(iv[0]), zip(items, vectors)))
        try:
            fitems, fvectors = map(list, zip(*filtered))
        except:
            fitems, fvectors = items, vectors
        _, index = Extractor.__find_center(fvectors)
        return items.index(fitems[index])

    def get_keywords(self, id: itemID, top: int = 100) -> List[str]:
        items, vectors = map(list, zip(*self.__c.dumps[id]))
        mean, index = Extractor.__find_center(vectors)
        counter = self.__c.vocab_count[id]

        def _get_f(t: wID) -> float:
            return float(counter[t])
        def _get_tf(t: wID) -> float:
            max_f = max([_get_f(w) for w in counter.keys() ])
            return .5 + (.5 * _get_f(t) / max_f)
        def _get_idf(t: wID) -> float:
            return 0.01 + normalize(len(self.__c.items)/len(self.__c.dumps[id]))

        def _get_score(t: wID) -> float:
            return _get_tf(t) * _get_idf(t) + _get_f(t) * 0.01

        words = [(w, _get_score(w)) for w in counter.keys()]
        return sorted(words, key=lambda w: -float(w[1]))[:top]

    def get_quotation(self, items: List[Item], vectors: np.ndarray) -> List[str]:
        pass