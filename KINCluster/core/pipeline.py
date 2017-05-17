from typing import Iterator

from KINCluster.core.item import Item

class Pipeline:
    def __init__(self):
        pass

    def capture_item(self) -> Iterator[Item]:
        """grab items
            :must be item generater
        """
        raise Exception('Override capture_item function to generator<Item>')

    def dress_item(self, item: Item):
        """dress item
            :item (has element extractable)
                - items     : cluster items
                - vectors   : cluster vectors
                - counter   : cluster counter
        """
        pass

    def __finalize__(self):
        pass
