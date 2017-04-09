# cluster type
CLUSTER_TYPE = "hcluster"

# threshold, recommand between 2, 32
THRESHOLD = 12

# # DB_SETTING
# DB_HOST='175.207.13.225'
# DB_USER='memento'
# DB_PASSWORD='memento@0x100_'
# DB_DB='memento'
# DB_CHARSET='utf8'

# pipeline
PIPELINES = [
]

# item element setting
ITEM_ELEMENT = [
    'title',
    'content',
    'date',
    'keyword'
]

STOP_WORDS = [
]

# tokens
TOKEN_POS_TAG = [
    'N*'
]
TOKEN_NEG_TAG = [
]
TOKEN_ZIP_TAG = [
    ['N*', 'SL'],
    
]

# user custom hyperparameter
ITEM_TITLE_RATE     = 10
ITEM_CONTENT_RATE   = 1
ITEM_DATE_RATE      = 5
ITEM_KEYWORD_RATE   = 20