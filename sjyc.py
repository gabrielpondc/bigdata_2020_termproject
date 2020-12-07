#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import math

from collections import defaultdict

import xsd
import csh


class suijiyuce:

    def __init__(self, n_jilu_dianying=10, bc_mx=True):

        print("Model:Random Predict.\n")
        print('-' * 80)
        self.n_jilu_dy = n_jilu_dianying
        self.xlji = None
        self.bc_mx = bc_mx

    def sh(self, xlj):

        mx_gl = csh.mxgl()
        try:
            self.dy_zmd = mx_gl.jz_mx('movie_popular')
            self.dy_jx = mx_gl.jz_mx('movie_count')
            self.xlji = mx_gl.jz_mx('trainset')
            self.sy_dy = mx_gl.jz_mx('total_movies')
            print('Load model(Done)\n')
            print('-' * 80)
        except OSError:
            print('Can not found trained model.\nTrain a new model.')
            self.xlji = xlj
            self.dy_zmd, self.dy_jx = xsd.js_dy_rq(xlj)
            self.sy_dy = list(self.dy_zmd.keys())
            print('Train a new model(Done)')
            print('-' * 80)
            if self.bc_mx:
                mx_gl.bc_mx(self.dy_zmd, 'movie_popular')
                mx_gl.bc_mx(self.dy_jx, 'movie_count')
                mx_gl.bc_mx(self.sy_dy, 'total_movies')
                print('Save the new model(Done)\n')
                print('-' * 80)
    def tuijian(self, yh):

        if not self.n_jilu_dy or not self.xlji or not self.dy_zmd or not self.dy_jx:
            raise NotImplementedError('Method has not called yet.')
        ni = self.n_jilu_dy
        yc_dy = list()
        jk_dy = self.xlji[yh]
        while len(yc_dy) < ni:
            dy = random.choice(self.sy_dy)
            if dy not in jk_dy:
                yc_dy.append(dy)
        return yc_dy[:ni]

    def cs(self, csj):
        if not self.n_jilu_dy or not self.xlji or not self.dy_zmd or not self.dy_jx:
            raise ValueError('Method has not called yet.')
        self.ceshiji = csj
        print('-' * 80)
        print('Start:Test recommendation system ')
        ni = self.n_jilu_dy
        jida = 0
        jilu_jihe = 0
        ceshi_jihe = 0
        sy_jl_dy = set()
        rq_hj = 0
        cs_sj = csh.cssj(dayinbushu=1000)
        for gd, yh in enumerate(self.xlji):
            cs_dy = self.ceshiji.get(yh, {})
            jl_dy = self.tuijian(yh)
            for dy in jl_dy:
                if dy in cs_dy:
                    jida += 1
                sy_jl_dy.add(dy)
                rq_hj += math.log(1 + self.dy_zmd[dy])
            jilu_jihe += ni
            ceshi_jihe += len(cs_dy)
            cs_sj.js_sj()
        xmd = jida / (1.0 * jilu_jihe)
        zhaohui = jida / (1.0 * ceshi_jihe)
        zy = len(sy_jl_dy) / (1.0 * self.dy_jx)
        rqz = rq_hj / (1.0 * jilu_jihe)
        f_s = (xmd * zhaohui * 2.0) / (xmd + zhaohui)
        print('Run test recommendation system(Done)')
        cs_sj.js()
        print('-' * 90)
        print('precision=%.4f\trecall=%.4f\tF-Measure1=%.4f\tcoverage=%.4f\tpopularity=%.4f\n' %
              (xmd, zhaohui,f_s, zy, rqz))
        print('-' * 90)
    def yuce(self, csj):
        dy_tj = defaultdict(list)
        print('-' * 80)
        print('start to predict scores ')
        yc_sj = csh.cssj(dayinbushu=500)
        for gd, yh in enumerate(csj):
            jl_sj = self.tuijian(yh)
            dy_tj[yh].append(jl_sj)
            yc_sj.js_sj()
            print('Predict scores(Done)')
            print('-' * 80)
        yc_sj.js()
        return dy_tj
