# -*- coding = utf-8 -*-
import csh
from jywpxtgl import jywpxtgl
from jyyhxtgl import jyyhxtgl
from sjj import sjj
from sjyc import suijiyuce
from csh import cssj
import sys

def mx_yx(mx_mc, sjj_mc, cs_dx=0.3, aqcs=False):
    print('-' * 70)
    print('\tModel: %s  Train set: %s  Test Size = %.2f' % (mx_mc, sjj_mc, cs_dx))
    print('-' * 70 + '\n')
    mx_glq = csh.mxgl(sjj_mc, cs_dx)
    try:
        xlj = mx_glq.jz_mx('trainset')
        csj = mx_glq.jz_mx('testset')
    except OSError:
        pfz = sjj.jzsjj(mc=sjj_mc)
        xlj, csj = sjj.xl_cs_fz(pfz, cs_dx=cs_dx)
        mx_glq.bc_mx(xlj, 'trainset')
        mx_glq.bc_mx(csj, 'testset')
    dy_wj, shuju = sjj.jz_xx(sjj_mc)
    mx_glq.ql_gzz(aqcs)
    if mx_mc == 'UserCF':
        mx = jyyhxtgl()
    elif mx_mc == 'ItemCF':
        mx = jywpxtgl()
    elif mx_mc == 'Random':
        mx = suijiyuce()
    elif mx_mc == 'UserCF-IIF':
        mx = jyyhxtgl(sy_xt_xsd=True)
    elif mx_mc == 'ItemCF-IUF':
        mx = jywpxtgl(yh_xt_xsd=True)
    else:
        raise ValueError('Can not recognize model' + mx_mc)
    mx.sh(xlj)
    dy_bl = jianli_dy_dt(dy_wj, shuju)
    tuijian_cs(mx, [1, 432, 123, 244, 166], dy_bl)
    mx.cs(csj)


def tuijian_cs(mx, yh_lb, dy_ditu):
    for yh in yh_lb:
        tuijian = mx.tuijian(str(yh))
        zhi=0
        print("\nRecommend for userid = %s:" % yh)
        for xiangmu in tuijian:
            zhi=zhi+1
            print(str(zhi) +":" + dy_ditu[xiangmu])

def jianli_dy_dt(wenjian, shuju):
    jieuo = {}
    with open(wenjian, encoding='unicode_escape') as sjl:
        hangs = sjl.readlines()
        for hang in hangs:
            hdz = hang.strip().split(shuju)
            jieuo[hdz[0]] = hdz[1]
    
    return jieuo



if __name__ == '__main__':
    xt_sj = cssj(danzi="Main Function")
    print('-' * 80)
    print('\t GU JIAKAI 20161795\tWEN JIALI 20174950\t LIU JIAQI 20173122')
    print('-' * 80 + '\n')
    print('\t\tRecommend System for Movielens ')
    print('-' * 70)
    print('\t 1:ml-100k\t2:ml-1m\t3:ml-25m')
    print('-' * 70 + '\n')
    a = int(input("Select Data set:"))
    sjj_mc = None
    mx_mc = None
    if a == 1:
        sjj_mc = 'ml-100k'

    elif a == 2:
        sjj_mc = 'ml-1m'
    elif a == 3:
        sjj_mc = 'ml-25m'
    else:
        print("No such number support")
    print('\r', end='', flush=True)
    print('-' * 80)
    print('\t1:UserCF\t2:UserCF-IIF\t3:ItemCF\t4:ItemCF-IUF\t5:Random')
    print('-' * 80 + '\n')
    b = int(input("Select model:"))
    if b == 1:
        mx_mc = 'UserCF'
    elif b == 2:
        mx_mc = 'UserCF-IIF'
    elif b == 3:
        mx_mc = 'ItemCF'
    elif b == 4:
        mx_mc = 'ItemCF-IUF'
    elif b == 5:
        mx_mc = 'Random'
    else:
        print("No such number support")
        sys.exit()
    print('\r', end='', flush=True)
    cs_dx = float(input("Test size:"))
    print('\r', end='', flush=True)
    mx_yx(mx_mc, sjj_mc, cs_dx, False)
    xt_sj.js()
