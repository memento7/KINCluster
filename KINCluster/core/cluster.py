from KINCluster.core.item import Item
from KINCluster.lib.tokenizer import tokenizer
from KINCluster import settings

from typing import List, Iterator, Union, Any
from collections import Counter

import numpy as np
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from scipy.cluster import hierarchy as hcluster
from scipy.cluster import vq as vq

class Cluster:
    def __init__(self, **kwargs):
        """hyperparameters
            :alpha = learning rate
            :min_alph = minimum learning reate
            :window = max value of vector
            :size = vector size
            :tokenizer = lambda document: str -> list or words: List[str]
        """
        self.settings = kwargs.get('settings', settings)
        alpha = kwargs.get("alpha", self.settings.C_LEARNING_RATE)
        min_alpha = kwargs.get("min_alpha", self.settings.C_LEARNING_RATE_MIN)
        window = kwargs.get("window", self.settings.C_WINDOW)
        size = kwargs.get("size", self.settings.C_SIZE)
        self.trate = kwargs.get("trate", self.settings.C_TRANING_RATE)
        self.epoch = kwargs.get("epoch", self.settings.C_EPOCH)
        self.thresh = kwargs.get("thresh", self.settings.C_THRESHOLD)
        self.tokenizer = tokenizer.s[kwargs.get("tokenizer", settings.C_TOKENIZER)]

        self.model = Doc2Vec(alpha=alpha, min_alpha=min_alpha, window=window, size=size)
        self._items = []
        self._counters = []
        self._vectors = []
        self._clusters = []
        self._dumps = []

    def put_item(self, item: Item):
        self._items.append(item)

    def __vocabs(self) -> Iterator[TaggedDocument]:
        for idx, item in enumerate(self._items):
            token = self.tokenizer(repr(item))
            self._counters.append(Counter(token))
            yield TaggedDocument(token, ['line_%s' % idx])

    def __documents(self) -> Iterator[TaggedDocument]:
        for idx, item in enumerate(self._items):
            yield TaggedDocument(self.tokenizer(str(item)), ['line_%s' % idx])

    def __cluster(self, method, metric, criterion) -> np.ndarray:
        return hcluster.fclusterdata(self._vectors, self.thresh, method=method, metric=metric, criterion=criterion)

    def cluster(self):
        # COMMENT: Top keyword 만 잘라서 분류해보기
        # 
        """cluster process
            : build vocab, using repr of item
            : train items, using str of item
            : get _vectors and _clusters
        """
        self.model.build_vocab(self.__vocabs())

        documents = list(self.__documents())
        for epoch in range(self.epoch):
            self.model.train(documents)
            self.model.alpha *= self.trate
            self.model.min_alpha = self.model.alpha

        self._vectors = np.array(self.model.docvecs)
        self._clusters = self.__cluster(self.settings.C_METHOD, self.settings.C_METRIC, self.settings.C_CRITERION)

        dumps = {c: [] for c in self.unique}
        for c, item, vector, counter in zip(self._clusters, self._items, self._vectors, self._counters):
            dumps[c].append((item, vector, counter))
        self._dumps = list(dumps.values())

    def similar(self, pos, neg=[], top=10):
        return self.model.most_similar(positive=pos,negative=neg,topn=top)

    @property
    def items(self) -> List[Item]:
        return self._items
    @property
    def vocab(self) -> List[str]:
        return self.model.vocab
    @property
    def vocab_count(self) -> List[Counter]:
        return self._counters
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
    @property
    def distribution(self) -> np.ndarray:
        return Counter(self._clusters)

    def __len__(self):
        return len(self._clusters)