# -*- coding: utf-8 -*-
"""
    tests.cluster
    ---------------
    Test cluster of KINCluster
    :author: MaybeS(maytryark@gmail.com)
"""

import pytest

from core.cluster import Cluster 
from core.pipeline import Pipeline 
from core.item import Item
from lib.tokenizer import stemize

test_text = ['2016헌나1.txt', '2014헌나1.txt']
test_keyword = ['헌법판결문', '헌법판결문']
class Pipeline(Pipeline):
    def capture_item(self):
        for text, keyword in zip(test_text, test_keyword):
            with open('tests/data/' + text) as f:
                content = f.read()
            yield Item(title=text,content=content,keyword=keyword,date='')
    def dress_item(self, items):
        for item in items:
            assert isinstance(item, Item)

def test_cluster1() :
    """ Testing for cluster, using test data
    """
    cluster = Cluster(epoch=32, tokenizer=stemize)
    pipeline = Pipeline()
    for item in pipeline.capture_item():
        cluster.put_item(item)
    cluster.cluster()

    assert '캠프' in list(map(list, zip(*cluster.similar('노무현'))))[0]
    assert '사건' in list(map(list, zip(*cluster.similar('박근혜'))))[0]
    assert len(test_text) == len(cluster.clusters)
    assert len(test_text) >= len(cluster.unique)

    for items in cluster.dumps:
        pipeline.dress_item(items)