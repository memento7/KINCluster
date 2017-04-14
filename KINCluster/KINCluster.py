from core.cluster import Cluster 
from core.pipeline import Pipeline 
from core.extractor import Extractor 
from lib.tokenizer import tokenize
import settings

class KINCluster:
    def __init__(self, pipeline, cluster=Cluster, Extractor=Extractor):
        self.pipeline = pipeline
        self.cluster = Cluster()
        self.Extractor = Extractor

    def run(self):
        for item in self.pipeline.capture_item():
            self.cluster.put_item(item)
        self.cluster.cluster()

        extractor = self.Extractor(self.cluster)
        for idx, dump in enumerate(self.cluster.dumps):
            items, vectors = map(list, zip(*dump))
            extracted = extractor.dump(idx)
            self.pipeline.dress_item(extracted, items)