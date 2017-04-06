from core.item import Item
import settings

from typing import List, Iterator, Any

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
        self.trate = kwargs.get("trate", 0.98)
        self.epoch = kwargs.get("epoch", 11)
        self.thresh = kwargs.get("thresh", settings.THRESHOLD)

        self.model = Doc2Vec(alpha=alpha, min_alpha=min_alpha, window=window)
        self._items = []
        self._vocab = []
        self._vectors = []
        self._clusters = []
        self._dumps = []

    def put_item(self, item: Item):
        self._items.append(item)

    def put_vocab(self, vocab: str):
        self._vocab.append(vocab)

    def __vocabs(self) -> Iterator[LabeledSentence]:
        for idx, vocab in enumerate(self.vocab):
            yield LabeledSentence(vocab, ['line_%s' % idx])

    def __setences(self) -> Iterator[LabeledSentence]:
        for idx, item in enumerate(self._items):
            yield LabeledSentence(str(item), ['line_%s' % idx])

    def __cluster(self):
        return hcluster.fclusterdata(self._vectors, self.thresh, criterion="distance")

    def cluster(self):
        """
            documents must be list of list.
        """
        self.model.build_vocab(self.__vocabs())

        for epoch in range(self.epoch):
            self.model.train(self.__setences())
            self.model.alpha *= self.trate
            self.model.min_alpha = self.model.alpha

        self._vectors = np.array(self.model.docvecs)
        self._clusters = self.__cluster()

        dumps = dict.fromkeys(self.unique(), [])
        for item, c in zip(self._items, self._clusters):
            dumps[c].append(item)
        self._dumps = list(dumps.values())

    @property
    def vocab(self) -> List[str]:
        return self._vocab or [repr(item) for item in self._items]
    @property
    def dumps(self) -> List[List[Item]]:
        return self._dumps
    @property
    def vecs(self) -> List[Any]:
        return self._vectors
    @property
    def unique(self) -> List[int]:
        return np.unique(self._clusters)
    @property
    def clusters(self) -> List[int]:
        return self._clusters
    def __len__(self):
        return len(self._clusters)