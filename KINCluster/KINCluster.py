from core.cluster import Cluster 
from core.pipeline import Pipeline 
import settings

pipe = Pipeline()
cluster = Cluster()

for item in pipe.capture_item():
    cluster.put_item(item)

cluster.cluster()

for items in cluster.dumps():
    pipe.dress_item(items)