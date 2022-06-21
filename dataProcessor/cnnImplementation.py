import numpy as np
import os

from jsonMuncher import jsonDigest
from model_converter import converter

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv1D, MaxPooling1D
from tensorflow.keras.utils import to_categorical



data, answers = jsonDigest()


data = tf.keras.utils.normalize(data)
answers = to_categorical(answers, 4)



model = Sequential()

model.add(Conv1D(filters=28, kernel_size=4, input_shape=data.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling1D(pool_size=4))

model.add(Conv1D(filters=28, kernel_size=4))
model.add(Activation("relu"))
model.add(MaxPooling1D(pool_size=4))

model.add(Flatten())
model.add(Dense(64))
#model.add(Flatten())
model.add(Dense(4, activation="softmax"))

model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=['accuracy'])

model.fit(data, answers, batch_size=32, epochs=50, validation_split=0.2)

converter(model)
#savePath = "./models/" + modelName + ".h5"
#if os.path.isfile(savePath) is False:
#	model.save(savePath)


 