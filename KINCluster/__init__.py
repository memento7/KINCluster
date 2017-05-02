"""
KINCluster is clustering like KIN.

release note: 
- version 0.1.5.5
    fix using custom settings
    support both moudle and dict

- version 0.1.5.4
    Update tokenizer, remove stopwords eff

- version 0.1.5.3
    now custom setting available.
    see settings.py

- version 0.1.5.2
    change item, extractor, pipeline module
    now, pipeline.dress_item pass just item(extractor.dump)
    fix prev versions error (too many value to unpack)
"""

__version__ = '0.1.5.5'

__all__ = ['KINCluster', 
'Cluster', 'Extractor', 'Item', 'Pipeline', 
'tokenizer', 'stopwords']

from KINCluster.KINCluster import KINCluster

from KINCluster.core.cluster import Cluster 
from KINCluster.core.extractor import Extractor 
from KINCluster.core.item import Item 
from KINCluster.core.pipeline import Pipeline 

from KINCluster.lib.tokenizer import tokenizer 
from KINCluster.lib.stopwords import stopwords 