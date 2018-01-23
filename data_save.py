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

import numpy as np
import mxnet as mx
import datetime
starttime = datetime.datetime.now()
sym,args,aux=mx.model.load_checkpoint('/cd/to/your/params/file/ssd-vgg_vgg16_reduced_512',0)
names = args.keys()
index = dict()
for i,name in enumerate(names):
    if 'weight' in name:
        data = []
        layer_para = args[name]
        shape = layer_para.shape
        data_mean = np.zeros((shape[0],shape[1]))
        data_std = np.zeros((shape[0],shape[1]))
        data_sum = np.zeros((shape[0],shape[1]))
        for j in range(shape[0]):
            for k in range(shape[1]):
                array = layer_para[j,k,:,:].asnumpy().flatten()
                m = np.mean(array)
                s = np.std(array)
                sum = np.sum(np.abs(array))
                data_mean[j,k] = m
                data_std[j,k] = s
                data_sum[j,k] = sum
        data.append(data_mean)
        data.append(data_std)
        data.append(data_sum)
        index.update({name:data})

endtime = datetime.datetime.now()
print (endtime - starttime).seconds
import pickle
output = open('data-ssd-vgg-512.pkl', 'wb')
pickle.dump(index, output)
output.close()

