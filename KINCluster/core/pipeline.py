from core.item import Item
import lib.tokenizer
import settings

from typing import List, Iterator, Union, Any
nparray = Any

class Pipeline:
    def __init__(self):
        pass

    def capture_item(self) -> Iterator[Item]:
        """grab items
            :must be item generater
        """
        pass

    def dress_item(self, item: Item, items: List[Item]):
        """dress item
            :item (has element extractable)
            :items (clustered items)
        """
        pass

    def __finalize__(self):
        pass