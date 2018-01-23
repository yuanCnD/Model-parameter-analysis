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

import matplotlib.pyplot as plt
import heapq
#cd to your log file, as example:
input = open('ssd_train_res_voc.log', 'r')

map = []
cross_loss = []
smoothl1_loss = []
loss = []

for lines in input:
    line = lines.split()
    if 'Validation-mAP' in line[-1]:
        map.append(float(line[-1].split('=')[-1]))
    if 'Train-CrossEntropy' in line[-1]:
        cross_loss.append(float(line[-1].split('=')[-1]))
    if 'Train-SmoothL1' in line[-1]:
        smoothl1_loss.append(float(line[-1].split('=')[-1]))
for i in range(len(cross_loss)):
    loss.append(cross_loss[i] + smoothl1_loss[i])
max_map = max(map)
min_loss = min(loss)

topNum = 5
top5max_map = heapq.nlargest(topNum, map)
top5min_loss = heapq.nsmallest(topNum, loss)
for i in range(topNum):
  print ('map  = {} and the epoch is {}'.format(str(top5max_map[i]), str(map.index(top5max_map[i]))))
  print ('loss = {}'.format(loss[map.index(top5max_map[i])]))
  print(' ')

for i in range(topNum):
  print ('map  = {} and the epoch is {}'.format(str(map[loss.index(top5min_loss[i])]), str(loss.index(top5min_loss[i]))))
  print ('loss = {}'.format(top5min_loss[i]))
  print(' ')

plt.figure('SSD')
plt.subplot(211)
plt.plot(map)
plt.grid(True)
plt.subplot(212)
plt.plot(loss)
plt.grid(True)
plt.show()