from core.item import Item
import lib.tokenizer
import settings

from typing import List, Iterator

class Pipeline:
    def __init__(self):
        pass

    def capture_item(self) -> Iterator[Item]:
        """grab items
            :must be item generater
        """
        pass

    def dress_item(self, items: List[Item]):
        """dress item
            :input items
            :dress up your items, ex) push to db
        """
        pass

    def __finalize__(self):
        pass