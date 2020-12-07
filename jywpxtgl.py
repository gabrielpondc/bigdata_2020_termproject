#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from operator import itemgetter
import math
import xsd
import csh
from csh import cssj
from collections import defaultdict




class jywpxtgl:

    def __init__(self, k_xsd_dy=20, n_jl_dy=10, yh_xt_xsd=False, bc_mx=True):
        print("Model:ItemBasedCF\n")
        print('-' * 80)
        self.k_xsd_dy = k_xsd_dy
        self.n_jl_dy = n_jl_dy
        self.xlj = None
        self.bc_mx = bc_mx
        self.yh_xt_xsd = yh_xt_xsd

    def sh(self, xlj):
        mxgl = csh.mxgl()
        try:
            self.dyxl_xsd_sz = mxgl.jz_mx(
                'movie_sim_mat-iif' if self.yh_xt_xsd else 'movie_sim_mat')
            self.dy_zmd = mxgl.jz_mx('movie_popular')
            self.dy_hj = mxgl.jz_mx('movie_count')
            self.xlj = mxgl.jz_mx('trainset')
            print('Load model(Done)\n')
            print('-' * 80)
        except OSError:
            print('Can not found trained model.\nTrain a new model.')
            self.dyxl_xsd_sz, self.dy_zmd, self.dy_hj = \
                xsd.js_wp_xsd(xlz=xlj,
                              yh_xsd_dd=self.yh_xt_xsd)
            self.xlj = xlj
            print('Train a new model(Done)')
            print('-' * 80)
            if self.bc_mx:
                mxgl.bc_mx(self.dyxl_xsd_sz,
                                         'movie_sim_mat-iif' if self.yh_xt_xsd else 'movie_sim_mat')
                mxgl.bc_mx(self.dy_zmd, 'movie_popular')
                mxgl.bc_mx(self.dy_hj, 'movie_count')
                mxgl.bc_mx(self.xlj, 'trainset')
                print('Save the new model((Done))\n')
                print('-' * 80)

    def tuijian(self, yh):
        if not self.dyxl_xsd_sz or not self.n_jl_dy or \
                not self.xlj or not self.dy_zmd or not self.dy_hj:
            raise NotImplementedError('Method has not called yet.')
        kdz = self.k_xsd_dy
        ndz = self.n_jl_dy
        yby_fs = collections.defaultdict(int)
        if yh not in self.xlj:
            print('The user (%s) can not found in the set.' % yh)
            return
        yk_dy = self.xlj[yh]
        for dy, pf in yk_dy.items():
            for zj_dy, xsd_dy in sorted(self.dyxl_xsd_sz[dy].items(),
                                                           key=itemgetter(1), reverse=True)[0:kdz]:
                if zj_dy in yk_dy:
                    continue
                yby_fs[zj_dy] += xsd_dy * pf
        return [dy for dy, _ in sorted(yby_fs.items(), key=itemgetter(1), reverse=True)[0:ndz]]

    def cs(self, csj):
        if not self.n_jl_dy or not self.xlj or not self.dy_zmd or not self.dy_hj:
            raise ValueError('Method has not called yet.')
        self.csj = csj
        print('-' * 80)
        print('Start to test recommendation system ')
        weizhi = self.n_jl_dy
        ddjd = 0
        jl_zs = 0
        cs_zs = 0
        sy_ji_zs = set()
        rq_hj = 0
        ceshishijian = cssj(dayinbushu=1000)
        for ni, yh in enumerate(self.xlj):
            ceshidy = self.csj.get(yh, {})
            jl_dy = self.tuijian(yh)
            for dy in jl_dy:
                if dy in ceshidy:
                    ddjd += 1
                sy_ji_zs.add(dy)
                rq_hj += math.log(1 + self.dy_zmd[dy])
            jl_zs += weizhi
            cs_zs += len(ceshidy)
            ceshishijian.js_sj()
        jqz = ddjd / (1.0 * jl_zs)
        sh = ddjd / (1.0 * cs_zs)
        fg = len(sy_ji_zs) / (1.0 * self.dy_hj)
        zmrq = rq_hj / (1.0 * jl_zs)
        f_s = (jqz * sh * 2.0) / (jqz + sh)
        print('Test recommendation system(Done)')
        ceshishijian.js()
        print('-' * 90)
        print('precision=%.4f\trecall=%.4f\tF-Measure1=%.4f\tcoverage=%.4f\tpopularity=%.4f\n' %
              (jqz, sh,f_s, fg, zmrq))
        print('-' * 90)

    def yuce(self, csj):
        dytuijian = defaultdict(list)
        print('-' * 80)
        print('start to predict scores ')
        ybyshijian = cssj(dayinbushu=500)
        for ni, yh in enumerate(csj):
            jl_dy = self.tuijian(yh)
            dytuijian[yh].append(jl_dy)
            ybyshijian.js_sj()
        print('Predict scores(Done)')
        print('-' * 80)
        ybyshijian.js()
        return dytuijian
