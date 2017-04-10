import settings

from typing import List, Any

class Item:
    def __init__(self, **kwargs):
        self._element = {}
        for k, v in kwargs.items():
            self._element[k] = v 

    def __str__(self) -> str:
        """represent text to clustering
            :apply n-gram or stemize if you need
        """
        return " ".join(map(str, self.element))

    def __repr__(self) -> str:
        """represent vocabs in item
        """
        return " ".join(map(str, self.element))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
           return other._element == self._element
        return False 

    @property
    def element(self) -> List[Any]:
        return [self._element[k] for k in self.element_keys]

    @property
    def element_keys(self) -> List[str]:
        return sorted(self._element.keys())
