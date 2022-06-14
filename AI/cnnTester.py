import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

import numpy as np

from choosers import choose, test


# 0 -> flick
# 1 -> fist
# 2 -> ring
# 3 -> like

modelName = "fast"

my_model = load_model("./models/" + modelName + ".h5")

myData = test()

# Due to complications in the javascript, we test the models without normalizing the data
# to get a better representation of the performance

# myData = tf.keras.utils.normalize(myData)



predictions = my_model.predict(myData)



prediction_list = predictions.tolist()

results = []

for each in prediction_list:
	index = each.index(max(each))
	if index == 0:
		print("flick")
	elif index == 1:
		print("fist")
	elif index == 2:
		print("like")
	elif index == 3:
		print("ring")
	else:
		print("error interpreting answer")




