from types import ModuleType
import logging

from KINCluster.core.cluster import Cluster
from KINCluster.core.extractor import Extractor
from KINCluster import settings as sets

class KINCluster:
    __log = logging
    __log.basicConfig(level=logging.INFO)

    def __init__(self, pipeline, cluster=Cluster, extractor=Extractor, settings={}):
        def getattrs(module):
            keys = [key for key in dir(module) if not key.startswith('__')]
            return {key: getattr(module, key) for key in keys}

        self.settings = getattrs(sets)

        if isinstance(settings, ModuleType):
            settings = getattrs(settings)
        if isinstance(settings, dict):
            for key, value in settings.items():
                self.settings[key] = value

        self.pipeline = pipeline
        self.cluster = cluster(settings=self.settings)
        self.extractor = extractor
        KINCluster.__log.info('KINCluster>> inited')

    def run(self):
        KINCluster.__log.info('KINCluster>> start running...')
        for item in self.pipeline.capture_item():
            self.cluster.put_item(item)
            
        KINCluster.__log.info('KINCluster>> start clustering...')
        self.cluster.cluster()
        KINCluster.__log.info('KINCluster>> done clustering.')

        KINCluster.__log.info('KINCluster>> start extracting...')
        extractor = self.extractor(self.cluster)
        for idx, _ in enumerate(self.cluster.dumps):
            self.pipeline.dress_item(extractor.dump(idx))
        KINCluster.__log.info('KINCluster>> done extracting...')
