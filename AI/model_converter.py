import tensorflow as ts
import tensorflowjs as tfjs
from tensorflow.keras.models import load_model


modelName = "fast"

my_model = load_model("./models/" + modelName + ".h5")

tfjs.converters.save_keras_model(my_model, './jsModels/' + modelName)