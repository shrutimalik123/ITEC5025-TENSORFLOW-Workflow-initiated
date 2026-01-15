import tensorflow as tf
import numpy as np

print("TensorFlow Version:", tf.__version__)

# Simple tensor operation
a = tf.constant([1.0, 2.0], dtype=tf.float32)
b = tf.constant([3.0, 4.0], dtype=tf.float32)
add = tf.add(a, b)

print("Tensor Addition Result:", add)
print("NumPy works too:", np.array([1, 2, 3]))

if add.numpy()[0] == 4.0:
    print("SUCCESS: TensorFlow is working correctly.")
else:
    print("FAILURE: Calculation incorrect.")
