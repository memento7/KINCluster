# -*- coding: utf-8 -*-
"""
    tests.cluster
    ---------------
    Test cluster of KINCluster
    :author: MaybeS(maytryark@gmail.com)
"""

import pytest

from KINCluster.core.extractor import Extractor, extractable
from KINCluster.core.cluster import Cluster 
from KINCluster.core.pipeline import Pipeline 
from KINCluster.core.item import Item
from KINCluster.lib.tokenizer import tokenize, stemize

import codecs

test_text = ['2016헌나1.txt', '2014헌나1.txt']
test_keyword = ['헌법판결문', '헌법판결문']

class Pipeline(Pipeline):
    def capture_item(self):
        for text, keyword in zip(test_text, test_keyword):
            with codecs.open('tests/data/' + text, 'r', 'utf-8') as f:
                content = f.read()
            yield Item(title=text,content=content,keyword=keyword,date='')

def test_extractor1():
    cluster = Cluster(epoch=32, tokenizer="tokenize")
    pipeline = Pipeline()
    for item in pipeline.capture_item():
        cluster.put_item(item)
    cluster.cluster()

    extractor = Extractor(cluster)

    for idx, dump in enumerate(cluster.dumps):
        items, vectors, counter = map(list, zip(*dump))
        
        assert set(['item_dump', 'vectors', 'counter', 'center', 'keywords']) == set(extractable.s.keys())
        
        extracted = extractor.dump(idx)

        assert isinstance(extracted, Item)
        assert isinstance(extracted.keywords, list)
        assert 32 == len(extracted.keywords)