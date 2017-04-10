from core.item import Item
import settings

from typing import List, Iterator, Any

import numpy as np

class Extractor():
    def __init__(self):
        pass

    def __find_center(self, vectors: np.ndarray) -> int:
        mean = np.mean(vectors)
        return int((np.abs(vectors - mean)).argmin())

    def get_topic(self, items: List[Item], vectors: np.ndarray, keyword: str) -> int:
        filtered = list(filter(labmda iv: keyword in iv[0], zip(items, vectors)))
        items, vectors = map(list, zip(*filtered))
        index = self.__find_center(vectors)
        return index

    def get_keywords(self, items: List[Item], vectors: np.ndarray, top: int = 10) -> List[str]:

        pass

    def get_quotation(self, items: List[Item], vectors: np.ndarray) -> List[str]:

        pass
