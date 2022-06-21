import tensorflow as ts
import tensorflowjs as tfjs
from tensorflow.keras.models import load_model



def converter(model):
	modelName = "fast2"

	#my_model = load_model("./models/" + modelName + ".h5")

	tfjs.converters.save_keras_model(model, './..//webserver/static/models/' + modelName)
	print("model " + modelName + " saved")