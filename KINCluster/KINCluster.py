from KINCluster.core.cluster import Cluster 
from KINCluster.core.pipeline import Pipeline 
from KINCluster.core.extractor import Extractor 
from KINCluster.lib.tokenizer import tokenize
from KINCluster import settings

class KINCluster:
    def __init__(self, pipeline, cluster=Cluster, Extractor=Extractor, settings=settings):
        self.pipeline = pipeline
        self.cluster = Cluster(settings=settings)
        self.Extractor = Extractor

    def run(self):
        for item in self.pipeline.capture_item():
            self.cluster.put_item(item)
        self.cluster.cluster()

        extractor = self.Extractor(self.cluster)
        for idx, dump in enumerate(self.cluster.dumps):
            self.pipeline.dress_item(extractor.dump(idx))