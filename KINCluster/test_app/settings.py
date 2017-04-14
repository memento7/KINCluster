# Cluster settings

### Methods = ["linkage", "single", "complete", "average", "weighted", "centroid", "median", "ward"]
C_METHOD="ward"
### Metrics = ["euclidean", "minkowski", "cityblock", "seuclidean", "sqeuclidean", "cosine", "correlation", "hamming", "jaccard", "chebyshev"]
C_METRIC="cosine"
### Criterions = ["inconsistent", "distance", "maxclust", "monocrit", "maxclust_monocrit"]
C_CRITERION="inconsistent"

# alpha
C_LEARNING_RATE = 0.025
# min_alpha
C_LEARNING_RATE_MIN = 0.025
# window
C_WINDOW = 5
# size
C_SIZE = 500
# trate
C_TRANING_RATE = 0.98
# epoch
C_EPOCH = 12
# threshold, recommand between 10-1, 10+1
C_THRESHOLD = 1.0

# tokenizer = ["tokenize", "stemize"]
# or implemeint in lib.tokenizer
C_TOKENIZER = "tokenize"

# Cluster type
## for now, only hcluster
C_TYPE = "hcluster"

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
ITEM_TITLE_RATE     = 10
ITEM_CONTENT_RATE   = 1
ITEM_DATE_RATE      = 5
ITEM_KEYWORD_RATE   = 20
