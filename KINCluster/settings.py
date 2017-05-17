# Cluster settings

### Methods = ["linkage", "single", "complete", "average", "weighted", "centroid", "median", "ward"]
METHOD = "ward"
### Metrics = ["euclidean", "minkowski", "cityblock", "seuclidean", "sqeuclidean", "cosine", "correlation", "hamming", "jaccard", "chebyshev"]
METRIC = "cosine"
### Criterions = ["inconsistent", "distance", "maxclust", "monocrit", "maxclust_monocrit"]
CRITERION = "inconsistent"

# alpha
LEARNING_RATE = 0.025
# min_alpha
LEARNING_RATE_MIN = 0.025
# window
WINDOW = 5
# size
SIZE = 500
# trate
TRANING_RATE = 0.98
# epoch
EPOCH = 64
# threshold, recommand between 10-1, 10+1
THRESHOLD = 1.15

# tokenizer = ["tokenize", "stemize"]
# or implemeint in lib.tokenizer
TOKENIZER = "tokenize"

# Cluster type
## for now, only hcluster
CLUSTER = "hcluster"

# item element setting
ITEM_ELEMENT = [
    'title',
    'content',
    'date',
    'keyword'
]


# Tokenizer setting
TOKEN_POS_TAG = [
]

TOKEN_NEG_TAG = [
]

TOKEN_ZIP_TAG = [
]

# user custom hyperparameter
ITEM_TITLE_RATE = 10
ITEM_CONTENT_RATE = 1
ITEM_DATE_RATE = 5
ITEM_KEYWORD_RATE = 20
