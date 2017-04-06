from core.item import Item
import settings

from typing import List, Iterator

class Pipeline:
    def __init__(self):
        pass

    def capture_item(self) -> Iterator[Item]:
        """
            grab items
        """
        pass

    def dress_item(self, items: List[Item]):
        """
            clustered items
        """
        pass

    def __finalize__(self):
        pass