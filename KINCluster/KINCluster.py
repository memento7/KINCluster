from KINCluster.core.cluster import Cluster 
from KINCluster.core.pipeline import Pipeline 
from KINCluster.core.extractor import Extractor 
from KINCluster.lib.tokenizer import tokenize
from KINCluster import settings as sets

from types import ModuleType

class KINCluster:
    def __init__(self, pipeline, cluster=Cluster, Extractor=Extractor, settings={}):
        def getattrs(module):
            keys = [k for k in dir(module) if not k.startswith('__')]
            return { key: getattr(module, key) for key in keys }

        self.settings = getattrs(sets)

        if isinstance(settings, ModuleType):
            settings = getattrs(settings)
        if isinstance(settings, dict):
            for k, v in settings.items():
                self.settings[k] = v

        self.pipeline = pipeline
        self.cluster = Cluster(settings=self.settings)
        self.Extractor = Extractor

    def run(self):
        for item in self.pipeline.capture_item():
            self.cluster.put_item(item)
        self.cluster.cluster()

        extractor = self.Extractor(self.cluster)
        for idx, dump in enumerate(self.cluster.dumps):
            self.pipeline.dress_item(extractor.dump(idx))