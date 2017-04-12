from core.item import Item
import settings

from typing import List, Iterator, Union, Any

import numpy as np
from gensim.models import Doc2Vec
from gensim.models.doc2vec import LabeledSentence
from scipy.cluster import hierarchy as hcluster
from scipy.cluster import vq as vq

class Cluster:
    def __init__(self, **kwargs):
        alpha = kwargs.get("alpha", 0.025)
        min_alpha = kwargs.get("min_alpha", 0.025)
        window = kwargs.get("window", 5)
        size = kwargs.get("size", 100)
        self.trate = kwargs.get("trate", 0.98)
        self.epoch = kwargs.get("epoch", 11)
        self.thresh = kwargs.get("thresh", settings.THRESHOLD)
        self.tokenizer = kwargs.get("tokenizer", lambda x: x.split())

        self.model = Doc2Vec(alpha=alpha, min_alpha=min_alpha, window=window, size=size)
        self._items = []
        self._vectors = []
        self._clusters = []
        self._dumps = []

    def put_item(self, item: Item):
        self._items.append(item)

    def __vocabs(self) -> Iterator[LabeledSentence]:
        for idx, item in enumerate(self._items):
            yield LabeledSentence(self.tokenizer(repr(item)), ['line_%s' % idx])

    def __setences(self) -> Iterator[LabeledSentence]:
        for idx, item in enumerate(self._items):
            yield LabeledSentence(self.tokenizer(str(item)), ['line_%s' % idx])

    def __cluster(self) -> np.ndarray:
        return hcluster.fclusterdata(self._vectors, self.thresh, criterion="distance")

    def cluster(self):
        """cluster process
            : build vocab, using repr of item
            : train items, using str of item
            : get _vectors and _clusters
        """
        self.model.build_vocab(self.__vocabs())

        for epoch in range(self.epoch):
            self.model.train(self.__setences())
            self.model.alpha *= self.trate
            self.model.min_alpha = self.model.alpha

        self._vectors = np.array(self.model.docvecs)
        self._clusters = self.__cluster()

        dumps = {c: [] for c in self.unique}
        for c, item, vector in zip(self._clusters,self._items,self._vectors):
            dumps[c].append((item, vector))
        self._dumps = list(dumps.values())

    def similar(self, pos, neg=[], top=10):
        return self.model.most_similar(positive=pos,negative=neg,topn=top)
    @property
    def vocab(self) -> List[str]:
        return self.model.vocab
    @property
    def dumps(self) -> List[List[Union[Item, np.ndarray]]]:
        return self._dumps
    @property
    def vectors(self) -> np.ndarray:
        return self._vectors
    @property
    def unique(self) -> np.ndarray:
        return np.unique(self._clusters)
    @property
    def clusters(self) -> np.ndarray:
        return self._clusters
    def __len__(self):
        return len(self._clusters)