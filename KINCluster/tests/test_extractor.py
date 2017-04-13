# -*- coding: utf-8 -*-
"""
    tests.cluster
    ---------------
    Test cluster of KINCluster
    :author: MaybeS(maytryark@gmail.com)
"""

import pytest

from core.extractor import Extractor 
from core.cluster import Cluster 
from core.pipeline import Pipeline 
from core.item import Item
from lib.tokenizer import tokenize, stemize

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
    cluster = Cluster(epoch=32, tokenizer=tokenize)
    pipeline = Pipeline()
    for item in pipeline.capture_item():
        cluster.put_item(item)
    cluster.cluster()

    extractor = Extractor(cluster)

    for idx, dump in enumerate(cluster.dumps):
        items, vectors = map(list, zip(*dump))

        topic_id = extractor.get_topic(idx, '탄핵')
        topic = items[topic_id]
        keywords = extractor.get_keywords(idx, 5)

        assert isinstance(topic_id, int)
        assert 5 == len(keywords)

if __name__ == '__main__':
    test_extractor1()