from os.path import dirname, join
from sys import path
path.append(join(dirname(__file__), '..'))

from KINCluster import KINCluster
from pipeline import PipelineServer
from test_app import settings

if __name__ == '__main__':
    kin = KINCluster(PipelineServer(), settings= settings)
    kin.run()