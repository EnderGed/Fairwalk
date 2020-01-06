#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:03:59 2019

Plots some of the plots in the paper

@author: enderged
"""
import matplotlib.pyplot as plt
import numpy as np

#
# stats = {'ogc': [62.25705329153605, 37.74294670846395],
#  'orc': [15.860109717868339, 80.7582288401254, 3.3816614420062696],
#  'wegc': [52.854399735501566, 47.145600264498434],
#  'werc': [31.56934022335423, 54.57623799960815, 13.854421777037617],
#  'wgc': [58.81887367750784, 41.18112632249216],
#  'wrc': [14.396686422413794, 82.04539331896552, 3.5579202586206895]}
#
#
# X = np.arange(2)
# plt.bar(X + 0.00, stats['ogc'], color = 'b', width = 0.25, label = 'network')
# plt.bar(X + 0.25, stats['wgc'], color = 'r', width = 0.25, label = 'original walk')
# plt.bar(X + 0.50, stats['wegc'], color = 'g', width = 0.25, label = 'fair walk')
# plt.xticks([0.25, 1.25], ['0', '1'])
# plt.xlabel('gender type')
# plt.ylabel('percentage')
# plt.legend()
#
# plt.show()
#
# X = np.arange(3)
# plt.bar(X + 0.00, stats['orc'], color = 'b', width = 0.25, label = 'network')
# plt.bar(X + 0.25, stats['wrc'], color = 'r', width = 0.25, label = 'original walk')
# plt.bar(X + 0.50, stats['werc'], color = 'g', width = 0.25, label = 'fair walk')
# plt.xticks([0.25, 1.25, 2.25], ['0', '1', '2'])
# plt.xlabel('gender type')
# plt.ylabel('percentage')
# plt.legend()
#
# plt.show()

#
# from supervised.plot_utils import *
# plot_recommendation_statistics('../data/la')

from graph_utils import *
from supervised.plot_utils import *


node2vec_evaluation_plot()

#plot_recommendation_statistics('../data/la', original=None)
plot_recommendation_statistics_lon_la(original=None)
plot_gender_race_walk_percentage('../data/la/counters.pick')

# regu = [0.103,0.103,0.115,0.387,0.272]
# fair = [0.068,0.068,0.054,0.288,0.234]
# improv = [(r-f)/r for r,f in zip(regu, fair)]
# print improv
# print np.mean(improv)
#
# regu = [0.112,0.112,0.176,0.474,0.298]
# fair = [0.095,0.095,0.135,0.417,0.282]
# improv = [(r-f)/r for r,f in zip(regu, fair)]
# print improv
# print np.mean(improv)
