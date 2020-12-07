
import collections
from operator import itemgetter

import math

from collections import defaultdict

import xsd
import csh
from csh import cssj

class jyyhxtgl:

    def __init__(self, k_xsd_yh=20, n_jl_dy=10, sy_xt_xsd=False, bc_mx=True):
        print("Model:UserBasedCF\n")
        print('-' * 80)
        self.k_xsd_yh = k_xsd_yh
        self.n_jl_dy = n_jl_dy
        self.xlj = None
        self.bc_mx = bc_mx
        self.sy_xt_xsd = sy_xt_xsd

    def sh(self, xlj):
        mx_glq = csh.mxgl()
        try:
            self.yh_xsd_sz = mx_glq.jz_mx(
                'user_sim_mat-iif' if self.sy_xt_xsd else 'user_sim_mat')
            self.dy_rqz = mx_glq.jz_mx('movie_popular')
            self.dy_hj = mx_glq.jz_mx('movie_count')
            self.xlj = mx_glq.jz_mx('trainset')
            print('Load model(Done)\n')
            print('-' * 80)
        except OSError:
            print('-' * 80)
            print('Can not found trained model.\nTrain a new model.')
            self.yh_xsd_sz, self.dy_rqz, self.dy_hj = \
                xsd.jx_yh_xsd(xlsjb=xlj,yh_csb_xsd=self.sy_xt_xsd)
            self.xlj = xlj
            print('Train a new model(Done)')
            print('-' * 80)
            if self.bc_mx:
                mx_glq.bc_mx(self.yh_xsd_sz,
                                         'user_sim_mat-iif' if self.sy_xt_xsd else 'user_sim_mat')
                mx_glq.bc_mx(self.dy_rqz, 'movie_popular')
                mx_glq.bc_mx(self.dy_hj, 'movie_count')
            print('Save the new model(Done)\n')
            print('-' * 80)

    def tuijian(self, yh):
        if not self.yh_xsd_sz or not self.n_jl_dy or \
                not self.xlj or not self.dy_rqz or not self.dy_hj:
            raise NotImplementedError('UserCF method has not called yet.')
        kz = self.k_xsd_yh
        weizhi = self.n_jl_dy
        yc_df = collections.defaultdict(int)
        if yh not in self.xlj:
            print('The user (%s) can not found in the set.' % yh)
            return
        yk_dy = self.xlj[yh]
        for xs_yh, xs_tz in sorted(self.yh_xsd_sz[yh].items(),
                                                      key=itemgetter(1), reverse=True)[0:kz]:
            for dy, pm in self.xlj[xs_yh].items():
                if dy in yk_dy:
                    continue

                yc_df[dy] += xs_tz * pm
        return [dy for dy, _ in sorted(yc_df.items(), key=itemgetter(1), reverse=True)[0:weizhi]]

    def cs(self, csj):

        if not self.n_jl_dy or not self.xlj or not self.dy_rqz or not self.dy_hj:
            raise ValueError('Method has not called yet.')
        self.csj = csj
        print('-' * 80)
        print('Start to test recommendation system ')
        weizhi = self.n_jl_dy
        jida = 0
        jl_hj = 0
        cs_hj = 0
        sy_jl_dy = set()
        rqzs = 0

        cs_sj = cssj(dayinbushu=1000)
        for w, yh in enumerate(self.xlj):
            cs_dy = self.csj.get(yh, {})
            jl_dy = self.tuijian(yh)
            for dy in jl_dy:
                if dy in cs_dy:
                    jida += 1
                sy_jl_dy.add(dy)
                rqzs += math.log(1 + self.dy_rqz[dy])
            jl_hj += weizhi
            cs_hj += len(cs_dy)
            cs_sj.js_sj()
        qxd = jida / (1.0 * jl_hj)
        hs = jida / (1.0 * cs_hj)
        fg = len(sy_jl_dy) / (1.0 * self.dy_hj)
        zmd = rqzs / (1.0 * jl_hj)
        f_s=(qxd*hs*2.0)/(qxd+hs)
        print('Run test recommendation system(Done)')
        print('-' * 80)
        cs_sj.js()
        print('-' * 90)
        print('precision=%.4f\trecall=%.4f\tF-Measure1=%.4f\tcoverage=%.4f\tpopularity=%.4f\n' %
              (qxd, hs,f_s, fg, zmd))
        print('-' * 90)
    def yuce(self, csj):
        dy_tj = defaultdict(list)
        print('-' * 80)
        print('start to predict scores ')
        yc_sj = cssj(dayinbushu=500)
        for w, yh in enumerate(csj):
            jl_dy = self.tuijian(yh)
            dy_tj[yh].append(jl_dy)
            yc_sj.js_sj()
        print('Predict scores(Done)')
        print('-' * 80)
        yc_sj.js()
        return dy_tj
