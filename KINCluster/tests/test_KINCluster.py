# -*- coding: utf-8 -*-
"""
    tests.KINCluster
    ---------------
    Test KINCluster
    :author: MaybeS(maytryark@gmail.com)
"""

import pytest

from core.cluster import Cluster 
from core.pipeline import Pipeline 
from core.extractor import Extractor 
from core.item import Item
from lib.tokenizer import tokenize, stemize

import codecs

test_text = ['2016헌나1.txt', '2014헌나1.txt']
test_keyword = ['헌법판결문', '헌법판결문']
# test_text = ['small.txt', 'small.txt']
# test_keyword = ['언어', '언어']

# Test1
class PipelineFile(Pipeline):
    def capture_item(self):
        for text, keyword in zip(test_text, test_keyword):
            with codecs.open('tests/data/' + text, 'r', 'utf-8') as f:
                content = f.read()
            yield Item(title=text,content=content,keyword=keyword,date='')

def test_app1():
    """ Testing for cluster, using test data
    """
    cluster = Cluster(epoch=32, tokenizer=stemize)
    pipeline = PipelineFile()

    for item in pipeline.capture_item():
        cluster.put_item(item)
    cluster.cluster()

    extractor = Extractor(cluster)
    for idx, dump in enumerate(cluster.dumps):
        items, vectors = map(list, zip(*dump))

        topic_id = extractor.get_topic(idx, '대통령')
        topic = items[topic_id]
        keywords = extractor.get_keywords(idx)

        print (keywords)
        pipeline.dress_item(items)

# Test2
import pymysql
SERVER_RDB = '175.207.13.225'
class PipelineServer(Pipeline):
    def __init__(self, keyword):
        self.keyword = keyword
    def capture_item(self):
        conn = pymysql.connect(host=SERVER_RDB,
                           user='memento',
                           password='memento@0x100_',
                           db='memento',
                           charset='utf8')
        cur = conn.cursor()

        columns = ['keyword', 'title', 'content', 'published_time']

        sql = "SELECT " + ",".join(columns) + " FROM articles where keyword like \'" + self.keyword  +"\' limit 1000"

        result = cur.execute(sql)

        for keyword, title, content, ptime in cur:
            yield Item(title=title,content=content,keyword=keyword,date=ptime)

        cur.close()
        conn.close()

def test_app2():
    """ Testing for cluster, using test data
    """
    cluster = Cluster(epoch=32, tokenizer=tokenize)
    pipe = PipelineServer('김태희')

    for item in pipe.capture_item():
        cluster.put_item(item)
    cluster.cluster()

    extractor = Extractor(cluster)
    for idx, dump in enumerate(cluster.dumps):
        items, vectors = map(list, zip(*dump))

        topic_id = extractor.get_topic(idx, '김태희')
        topic = items[topic_id]
        keywords = extractor.get_keywords(idx, 5)

        print (topic)
        print (keywords)
    print (cluster.distribution)

if __name__ == '__main__':
    test_app2()