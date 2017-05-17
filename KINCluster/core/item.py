from typing import List, Any
from collections import OrderedDict

class Item:
    def __init__(self, **kwargs):
        """item elements is ordered dict
        why?: str and repr must return same value always
        """
        self.__e = OrderedDict()
        for key, value in kwargs.items():
            try:
                setattr(self, key, value)
            except:
                raise "do not use item key like 'keys', 'items' or dumplicated key"
            self.__e[key] = value

    def __str__(self) -> str:
        """represent text to clustering
            :apply n-gram or stemize if you need
        """
        return " ".join(map(str, self.values))

    def __repr__(self) -> str:
        """represent vocabs in item
        """
        return " ".join(map(str, self.values))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__e == self.__e
        return False

    @property
    def values(self) -> List[Any]:
        """ return element values
        """
        return self.__e.values()

    @property
    def keys(self) -> List[Any]:
        """ return element keys
        """
        return self.__e.keys()
