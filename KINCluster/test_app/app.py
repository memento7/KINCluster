from os.path import dirname, join
from sys import path
path.append(join(dirname(__file__), '..'))

from KINCluster import KINCluster
from pipeline import PipelineTest

if __name__ == '__main__':
    kin = KINCluster(PipelineTest('박근혜'))
    kin.run()