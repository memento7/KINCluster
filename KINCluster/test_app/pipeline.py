from core.pipeline import Pipeline 
from core.item import Item
import settings

import pymysql

class PipelineServer(Pipeline):
    def __init__(self, start_date, end_date):
        self.sd = start_date
        self.ed = end_date
        
    def capture_item(self):
        conn = pymysql.connect(host     = settings.SERVER_RDB,
                               user     = settings.SERVER_USER,
                               password = settings.SERVER_PASS,
                               db       = settings.SERVER_DB,
                               charset  = 'utf8')
        cur = conn.cursor()

        columns = ['id', 'keyword', 'title', 'content', 'published_time', 'reply_count', 'href_naver']

        sql = "SELECT " + ",".join(columns) + " FROM articles where published_time between \'" +\
                self.sd + "\' and \'" + self.ed +"\'"

        result = cur.execute(sql)

        for idx, keyword, title, content, ptime, reply_count, href_naver in cur:
            yield Item(idx=idx,title=title,content=content,keyword=keyword,date=ptime,reply_count=reply_count,href_naver=href_naver)

        cur.close()
        conn.close()

    def dress_item(self, extracted, items):
        print ('size', len(items))
        print ('title', extracted.topic.title)
        print ('keywords', extracted.keywords)
        print ('quotation', extracted.quotation)
