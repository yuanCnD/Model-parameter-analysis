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
import numpy as np
pkl_file = open('data-filter.pkl', 'rb')
data1 = pickle.load(pkl_file)
pkl_file.close()
name = data1.keys()
filter = data1[name[0]][0]
mean = np.mean(abs(filter))
shape = filter.shape
txtName = "codingWord.txt"
f=file(txtName, "a+")
# for i in range(shape[1]):
for k in range(shape[0]):
    for j in range(9):
        new_context = str(int(filter[k,0,j]/mean*10)) + '\t'
        f.write(new_context)
    new_context = '\n'
    f.write(new_context)
f.close()