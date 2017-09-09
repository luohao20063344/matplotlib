# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 16:31:29 2016

@author: dell
"""

# plot all the points in the figure, and without any smooth steps.
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import sys
import argparse
from matplotlib import rc
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import MaxNLocator
import pandas as pd

if __name__ == '__main__':
    
    fig = plt.figure()
    fig.set_figwidth(15)
    ax = fig.add_subplot(313)
    mydf = pd.read_table('segment.txt', header = None)
    majorFormatter = FormatStrFormatter('%d')
    ax.xaxis.set_major_formatter(majorFormatter)
    ax.axes.get_xaxis().set_major_locator(MaxNLocator(5))
    ax.set_xlim(0, 8201357)
    ax.set_ylabel('GC Level (%)')
    length = 8201357
    gclist = []
    for item in mydf.values:
        #ax.axhline(y = item[3], xmin = item[0]/length, xmax = item[1]/length, color = 'r')
        ax.hlines(y = item[3], xmin = item[0], xmax = item[1], color = 'r')
        gclist.append(item[3])
    for i, item in enumerate(mydf.values):
        if i < len(mydf.values)-1:
            ax.vlines(x = item[1], ymin = min(gclist[i+1], item[3]), ymax = max(gclist[i+1], item[3]), color = 'r')
        
    #ax.axhline(y = 50)
    #plt.show()
        #tp = xrange(int(item[0]), int(item[1]))
        #ax.plot(tp, [item[3]]*len(tp), 'r-', label='Genomic island')
        #ax.
    
    #t1 = xrange(100000, 2000000)
    #ax.plot(t1, [0.5]*len(t1), 'r-', label='Genomic island')
