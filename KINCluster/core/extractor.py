from core.item import Item
from lib.tokenizer import stemize
import settings

from typing import List, Union, Any
from collections import Counter
from math import log10 as normalize
from itertools import chain

# type hinting
dID = int # document id
wID = str # word id, it str cuz word counter, {word: count}

import numpy as np

class Extractor():
    """you can redesign extractor
        - get_topic
        - get_keywords
        - get_quotation
    """
    def __init__(self, tokenizer=stemize):
        self.tokenizer = tokenizer

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
        words = set()
        item_counters = [Counter() for _ in items]
        for item_id, item in enumerate(items):
            for word in self.tokenizer(repr(item)):
                item_counters[item_id][word] += 1
                words.add(word)
        return (words, item_counters)

    def get_topic(self, items: List[Item], vectors: np.ndarray, keyword: str) -> int:
        filtered = list(filter(lambda iv: keyword in repr(iv[0]), zip(items, vectors)))
        fitems, fvectors = map(list, zip(*filtered))
        _, index = Extractor.__find_center(fvectors)
        return items.index(fitems[index])

    def get_keywords(self, items: List[Item], vectors: np.ndarray, top: int = 10) -> List[str]:
        mean, index = Extractor.__find_center(vectors)
        words, counters = self.__get_word_count(items)

        def _get_f(t: wID, d: dID) -> float:
            return float(counters[d][t])
        def _get_tf(t: wID, d: dID) -> float:
            w = (0.5) * _get_f(t, d)
            max_f = max([_get_f(w, d) for w, _ in counters[d].items() ])
            return 0.5 + (w / max_f) 
        def _get_idf(t: wID) -> float:
            return normalize(len([1 for counter in counters if t in counter]) / len(counters))

        return [(w, _get_tf(w, index) * _get_idf(w)) for w in words][:top]


    def get_quotation(self, items: List[Item], vectors: np.ndarray) -> List[str]:

        pass
