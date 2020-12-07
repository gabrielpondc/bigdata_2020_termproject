# -*- coding = utf-8 -*-

import time
import pickle
import os
import shutil
class cssj:

    def __init__(self, dayinbushu=20000, danzi=''):
        self.bs = 0
        self.DAYINBUSHU = dayinbushu
        self.KAISHI_SHIJIAN = time.time()
        self.danzi = danzi
        self.ZSJ = 0.0

    def js_sj(self):
        if self.bs % self.DAYINBUSHU == 0:
            czjsj = time.time()
            print(self.danzi + ' The Steps(%d) is spend %.2f seconds' % (
                self.bs, czjsj - self.KAISHI_SHIJIAN))
            print('-' * 80)
        self.bs += 1

    def js(self):
        print('-' * 80)
        print('Total spend %.2f seconds  \n' % self.hq_zo_sj())
        print('-' * 80)
    def hq_zx_bs(self):
        return self.bs

    def hq_zo_sj(self):
        return time.time() - self.KAISHI_SHIJIAN


class mxgl:
    lj_mc = ''

    @classmethod
    def __init__(cls, sj_mc=None, cs_dx=0.3):
        if not cls.lj_mc:
            cls.lj_mc = "model/" + sj_mc + '-testsize' + str(cs_dx)

    def bc_mx(self, mx, bc_sj: str):
        if 'pkl' not in bc_sj:
            bc_sj += '.pkl'
        if not os.path.exists('model'):
            os.mkdir('model')
        pickle.dump(mx, open(self.lj_mc + "-%s" % bc_sj, "wb"))

    def jz_mx(self, mx_mc: str):
        if 'pkl' not in mx_mc:
            mx_mc += '.pkl'
        if not os.path.exists(self.lj_mc + "-%s" % mx_mc):
            raise OSError('Can not find the model named %s / dir' % mx_mc)
        return pickle.load(open(self.lj_mc + "-%s" % mx_mc, "rb"))

    @staticmethod
    def ql_gzz(clean=False):
        if clean and os.path.exists('model'):
            shutil.rmtree('model')
