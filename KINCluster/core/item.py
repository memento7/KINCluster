from KINCluster import settings

from typing import List, Any

class Item:
    def __init__(self, **kwargs):
        self._element = {}
        for k, v in kwargs.items():
            setattr(self, k, v)
            self._element[k] = v

    def __str__(self) -> str:
        """represent text to clustering
            :apply n-gram or stemize if you need
        """
        return " ".join(map(str, self.items))

    def __repr__(self) -> str:
        """represent vocabs in item
        """
        return " ".join(map(str, self.items))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
           return other._element == self._element
        return False 

    @property
    def items(self) -> List[Any]:
        return [self._element[k] for k in self.keys]

    @property
    def keys(self) -> List[str]:
        """ return sorted element keys
        """
        return sorted(self._element.keys())
