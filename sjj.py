# -*- coding = utf-8 -*-
import collections
import os
import itertools
import random
from collections import namedtuple

jlsjb = namedtuple('Dataset', ['url', 'path', 'sep', 'reader_params'])

JL_SJZ = {
    'ml-100k':
        jlsjb(
            url='http://files.grouplens.org/datasets/movielens/ml-100k.zip',
            path='data/ml-100k/u.data',
            sep='\t',
            reader_params=dict(line_format='user item rating timestamp',
                               rating_scale=(1, 5),
                               sep='\t')
        ),
    'ml-1m'  :
        jlsjb(
            url='http://files.grouplens.org/datasets/movielens/ml-1m.zip',
            path='data/ml-1m/ratings.dat',
            sep='::',
            reader_params=dict(line_format='user item rating timestamp',
                               rating_scale=(1, 5),
                               sep='::')
        ),
    'ml-25m':
    jlsjb(
        url = 'http://files.grouplens.org/datasets/movielens/ml-25m.zip',
        path='data/ml-25m/ratings.csv',
        sep=',',
            reader_params=dict(line_format='user item rating timestamp',
                               rating_scale=(1, 5),
                               sep=',')
    )
}

random.seed(0)


class sjj:
    def __init__(self):
        pass

    @classmethod
    def jzsjj(cls, mc='ml-100k'):
        try:
            sjj = JL_SJZ[mc]
        except KeyError:
            raise ValueError('Unknown dataset ' + mc +
                             '. Accepted values are ' +
                             ', '.join(JL_SJZ.keys()) + '.')
        if not os.path.isfile(sjj.path):
            raise OSError("Can not found set Please download from"+sjj.url)
        with open(sjj.path) as f:
            _iter = itertools.islice(f, 0, None)
            if 'ml-25m' in sjj.path:
                next(_iter)
            pm = [cls.jx_h(line, sjj.sep) for line in _iter]
        print("Load " + mc + " dataset(Done) .")
        print('-' * 80)
        return pm

    @classmethod
    def jx_h(cls, hs: str, zb: str):
        yh, dy, pf = hs.strip('\r\n').split(zb)[:3]
        return yh, dy, pf

    @classmethod
    def xl_cs_fz(cls, phb, cs_dx=0.2):
        train, test = collections.defaultdict(dict), collections.defaultdict(dict)
        csj_cd = 0
        xlj_cd = 0
        for yh, dy, pm in phb:
            if random.random() <= cs_dx:
                test[yh][dy] = float(pm)
                xlj_cd += 1
            else:
                train[yh][dy] = float(pm)
                csj_cd += 1
        print('Split rating data to training set and test set(Done) ')
        print('-' * 80)
        print('train set size : %s' % csj_cd)
        print('test set size :%s\n' % xlj_cd)
        return train, test
    
    @classmethod
    def jz_xx(cls, mc):
        bg = {'ml-25m': ('data/ml-25m/movies.csv', ','),
        'ml-1m': ('data/ml-1m/movies.dat', '::'),
        'ml-100k': ('data/ml-100k/u.item', '|')}

        return bg[mc]

