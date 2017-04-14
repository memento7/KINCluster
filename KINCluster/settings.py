# Cluster settings
### Methods = ["linkage", "single", "complete", "average", "weighted", "centroid", "median", "ward"]
METHOD="ward"
### Metrics = ["euclidean", "minkowski", "cityblock", "seuclidean", "sqeuclidean", "cosine", "correlation", "hamming", "jaccard", "chebyshev"]
METRIC="cosine"
### Criterions = ["inconsistent", "distance", "maxclust", "monocrit", "maxclust_monocrit"]
CRITERION="inconsistent"

# Cluster type
## for now, only hcluster
CLUSTER_TYPE = "hcluster"

# threshold, recommand between 10-1, 10+1
THRESHOLD = 1.0

# item element setting
ITEM_ELEMENT = [
    'title',
    'content',
    'date',
    'keyword'
]

STOP_WORDS = [
]

# Tokenizer setting
TOKEN_POS_TAG = [
    'N*'
]

TOKEN_NEG_TAG = [
]

TOKEN_ZIP_TAG = [
    ['N*', 'SL'],    
]

# # DB_SETTING
# DB_HOST='175.207.13.225'
# DB_USER='memento'
# DB_PASSWORD='memento@0x100_'
# DB_DB='memento'
# DB_CHARSET='utf8'

# user custom hyperparameter
ITEM_TITLE_RATE     = 10
ITEM_CONTENT_RATE   = 1
ITEM_DATE_RATE      = 5
ITEM_KEYWORD_RATE   = 20
