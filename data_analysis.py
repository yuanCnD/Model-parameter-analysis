# Copyright 2018 yuanCnD.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import pickle
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pkl_file.close()
names = data1.keys()
names = sorted(names)
remain_index = []
fig_org_data = 1
fig_pic_data = -1
mea_list = []
var_list = []
list_name = []
for i,name in enumerate(names):
    order = name.split('_')[0][-1]
    # if  8>int(order)>1 and 'conv' in name.split('_')[0]:
    if 'conv7' in name:
        filter = data1[name]
        mean = filter[0]
        std = filter[1]
        sum = filter[2]
        shape = sum.shape

        mea_list.append(np.mean(sum))
        var_list.append(np.std(sum))
        list_name.append(name)

        if fig_org_data>0:
            fig = plt.figure()
            ax = Axes3D(fig)
            X = np.arange(0, shape[1], 1)
            Y = np.arange(0, shape[0], 1)
            X, Y = np.meshgrid(X, Y)
            ax.plot_surface(X, Y, sum, rstride=1, cstride=1, cmap='rainbow')
            plt.show()

        if fig_pic_data>0:
            for j in range(shape[1]):
                single_channel_sum =0
                for i in range(shape [0]):
                    single_channel_sum += sum[i,j]
                channel_mean = single_channel_sum/shape [0]
                if channel_mean > 0.1:
                    remain_index.append(j)
            for i in range(shape[0]):
                index_mean = []
                index_std = []
                label = []
                for j in remain_index:
                    index_mean.append(float(mean[i,j]))
                    index_std.append(float(std[i, j]))
                plt.figure('filter')
                plt.subplot(211)
                plt.title('filter mean')
                plt.plot(range(len(index_mean)),index_mean)
                plt.grid(True)
                label.append("filter%d"%(i+1))
                plt.legend(label, loc=0, ncol=2)
                plt.subplot(212)
                plt.title('filter std')
                plt.plot(range(len(index_std)),index_std)
                plt.grid(True)
                plt.legend(label, loc=0, ncol=2)
                plt.show()

grid = [[0] * 2] * len(list_name)
for i in range(len(list_name)):
    grid[i] = [mea_list[i],var_list[i]]
import matplotlib.pylab as pylab
params={
    'axes.labelsize': '35',
    'xtick.labelsize':'27',
    'ytick.labelsize':'27',
    'lines.linewidth':2 ,
    'legend.fontsize': '10',
    'figure.figsize'   : '24, 9'
}
pylab.rcParams.update(params)
ind = np.arange(2)                # the x locations for the groups
width = 0.05
for i in range(len(list_name)):
    plt.bar(ind+i*width, grid[i], width, label=list_name[i])

plt.xticks(np.arange(2) + 2.5*width, ('mean','std'))
axes = plt.gca()
axes.grid(True)
plt.legend(loc="upper right")
plt.show()