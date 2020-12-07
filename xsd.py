# -*- coding = utf-8 -*-
import collections
import math
from collections import defaultdict
from csh import cssj


def jx_yh_xsd(xlsjb, yh_csb_xsd=False):
    print('-' * 80)
    print('Build: movie-users inverse table')
    dydyh = collections.defaultdict(set)
    dyymd = defaultdict(int)

    for yh, dys in xlsjb.items():
        for dy in dys:
            dydyh[dy].add(yh)
            dyymd[dy] += 1
    print('Build: movie-users inverse table(Done)')
    print('-' * 80)

    dy_zh = len(dydyh)
    print('total movie number = %d' % dy_zh)
    print('-' * 80)
    print('Generate:user co-rated movies similarity matrix')
    yhxsd_sz = {}
    dydyh_sj = cssj(dayinbushu=1000)
    for dy, yhm in dydyh.items():
        for yh1 in yhm:
            yhxsd_sz.setdefault(yh1, defaultdict(int))
            for yh2 in yhm:
                if yh1 == yh2:
                    continue
                if yh_csb_xsd:
                    yhxsd_sz[yh1][yh2] += 1 / math.log(1 + len(yhm))
                else:
                    yhxsd_sz[yh1][yh2] += 1
        dydyh_sj.js_sj()
    print('Generate: user co-rated movies similarity matrix(Done)')
    print('-' * 80)
    dydyh_sj.js()
    print('-' * 80)
    print('Calculate matrix: user-user similarity ')
    yh_xsd_sz = cssj(dayinbushu=1000)
    for yh1, zj_yh in yhxsd_sz.items():
        yh1_cd = len(xlsjb[yh1])
        for yh2, js in zj_yh.items():
            yh2_cd = len(xlsjb[yh2])
            yhxsd_sz[yh1][yh2] = js / math.sqrt(yh1_cd * yh2_cd)
        yh_xsd_sz.js_sj()

    print('Calculate: user-user similarity(Done)')
    print('-' * 80)
    yh_xsd_sz.js()
    return yhxsd_sz, dyymd, dy_zh


def js_wp_xsd(xlz, yh_xsd_dd=False):
    dy_rq, dy_jx = js_dy_rq(xlz)
    print('-' * 80)
    print('Generate: items co-rated similarity matrix')
    dy_xsd_sz = {}
    dydyh_sj = cssj(dayinbushu=1000)
    for yh, dys in xlz.items():
        for dy in dys:
            dy_xsd_sz.setdefault(dy, defaultdict(int))
            for dy2 in dys:
                if dy == dy2:
                    continue
                if yh_xsd_dd:
                    dy_xsd_sz[dy][dy2] += 1 / math.log(1 + len(dys))
                else:
                    dy_xsd_sz[dy][dy2] += 1
        dydyh_sj.js_sj()
    print('Generate:items co-rated similarity matrix.(Done)')
    print('-' * 80)
    dydyh_sj.js()
    print('-' * 80)
    print('Calculate: item-item similarity matrix')

    dy_xs_sz_sj = cssj(dayinbushu=1000)
    for dy, zj_wp in dy_xsd_sz.items():
        dy1_cd = dy_rq[dy]
        for dy2, jx in zj_wp.items():
            yh2_cd = dy_rq[dy2]
            dy_xsd_sz[dy][dy2] = jx / math.sqrt(dy1_cd * yh2_cd)
        dy_xs_sz_sj.js_sj()

    print('Calculate:item-item similarity matrix(Done)')
    print('-' * 80)
    dy_xs_sz_sj.js()
    return dy_xsd_sz, dy_rq, dy_jx


def js_dy_rq(xlj):
    dy_zmd = defaultdict(int)
    print('-' * 80)
    print('Counting : Movies number and popularity')

    for yh, dys in xlj.items():
        for dy in dys:
            dy_zmd[dy] += 1
    print('Count: Movies number and popularity(Done)')
    print('-' * 80)
    dy_jx = len(dy_zmd)
    print('Total movie: %d' % dy_jx)
    return dy_zmd, dy_jx
