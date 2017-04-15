from KINCluster.core.item import Item
from KINCluster.lib import tokenizer
from KINCluster import settings

from typing import List, Iterator, Union, Any
nparray = Any

class Pipeline:
    def __init__(self):
        pass

    def capture_item(self) -> Iterator[Item]:
        """grab items
            :must be item generater
        """
        raise Exception('Override capture_item function to generator<Item>')
        pass

    def dress_item(self, item: Item, items: List[Item]):
        """dress item
            :item (has element extractable)
            :items (clustered items)
        """
        pass

    def __finalize__(self):
        pass