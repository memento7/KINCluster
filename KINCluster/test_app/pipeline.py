from core.pipeline import Pipeline 
from core.item import Item

import pymysql

SERVER_RDB = '175.207.13.225'
class PipelineTest(Pipeline):
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

    def dress_item(self, extracted, items):
        print ('size', len(items))
        print ('title', extracted.topic.title)
        print ('keywords', extracted.keywords)
        print ('quotation', extracted.quotation)
