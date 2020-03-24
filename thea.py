###test param in dilation


import os
import numpy as np
import keras.layers as L
import keras.backend as K
from layer_test import set_keras_backend
import importlib
from keras.engine import Model, Input

## Using Theano as Keras backend.
## Input dtype default is float32

layer = 'DepthwiseConv2D'  # or 'Conv2D'
#kwargs for DepthwiseConv2D
kwargs={
  'data_format': 'channels_first',
  'dilation_rate': 0,
  'kernel_size': 3, 
  'padding': 'valid', 
  'strides': 3}

# kwargs for Conv2D
# kwargs = {
# 'filters': 9, 
# 'kernel_size': 4,
# 'padding': 'valid', 
# 'strides': 4, 
# 'dilation_rate': 0, 
# 'data_format': 'channels_last'}
 
input_data = (10 * np.random.random((1,32,32,16)))
input = input_data.astype('float32')
model_path = os.path.join('./', 'model.h5')
layer_cls = getattr(L, layer)
layer = layer_cls(**kwargs)
x = Input(batch_shape=input.shape)
y = layer(x)
bk_model =Model(x, y)
bk_model.save(model_path, bk_model)
print('finish')
