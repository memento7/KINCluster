try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from KINCluster import __version__

setup(
    name = 'KINCluster',
    packages = ['KINCluster' ,'KINCluster/core', 'KINCluster/lib'],
    include_package_data=True,
    version = __version__,
    description = 'Korean Involute News Cluster',
    license = 'MIT',
    author = 'Bae jiun',
    author_email = 'alice.maydev@gmail.com',
    
    url = 'https://github.com/MaybeS/KINCluster',
    keywords = ['KINCluster', 'cluster', 'documents' 'doc2vec', 'tokenize', 'korean'],

    install_requires=[
        'gensim==0.13.4.1',
        'konlpy>=0.4.4',
        'scipy>=0.19.0',
        'numpy>=1.12.1+mkl'
    ],

    classifiers=(
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),

    entry_points={
        'console_scripts': [
            'jikji = jikji.cli:main',
        ],
    },
)