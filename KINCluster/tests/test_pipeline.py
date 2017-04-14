# -*- coding: utf-8 -*-
"""
    tests.pipeline
    ---------------
    Test pipeline of KINCluster
    :author: MaybeS(maytryark@gmail.com)
"""

import pytest

from core.pipeline import Pipeline 
from core.item import Item

class Pipeline(Pipeline):
    def capture_item(self):
        for v in range(10):
            yield Item(value=str(v))

    def dress_item(self, items):
        for item in items:
            assert isinstance(item, Item)

def test_pipeline1():
    """ Testing for pipeline
    """
    pipeline = Pipeline()
    items = [[], []]
    for item, v in zip(pipeline.capture_item(), range(10)):
        items[v % 2].append(item)
        assert item == Item(value=str(v))

    for dump in items:
        pipeline.dress_item(dump)