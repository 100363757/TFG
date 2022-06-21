import os
import json
import numpy as np


skeleton = ["wrist" ,"thumb-metacarpal", "thumb-phalanx-proximal", "thumb-phalanx-distal", "thumb-tip", 
    "index-finger-metacarpal", "index-finger-phalanx-proximal", "index-finger-phalanx-intermediate", "index-finger-phalanx-distal", "index-finger-tip", 
    "middle-finger-metacarpal", "middle-finger-phalanx-proximal", "middle-finger-phalanx-intermediate", "middle-finger-phalanx-distal", "middle-finger-tip", 
    "ring-finger-metacarpal", "ring-finger-phalanx-proximal", "ring-finger-phalanx-intermediate", "ring-finger-phalanx-distal", "ring-finger-tip", 
    "pinky-finger-metacarpal", "pinky-finger-phalanx-proximal", "pinky-finger-phalanx-intermediate", "pinky-finger-phalanx-distal", "pinky-finger-tip"]



def jsonDigest():
	once = True
	loadedData = []
	loadedAnswer = []

	for subdir, dirs, files in os.walk("./"):
		if subdir == "./0" or subdir == "./1" or subdir == "./2" or subdir == "./3":
			appendable = subdir.split("/")[1];	
			for file in files:
				
				filepath = subdir + os.sep + file
				base = open(filepath, 'r')
				loaded = json.load(base)
				frameTrain = []
				for frame in loaded['frames']:
					
					x_train = []

					rightHand = frame['right']
					for joint in skeleton:
					
						position = rightHand[joint]['position']
						orientation = rightHand[joint]['orientation']
						
						x_train.append(position['x'])
						x_train.append(position['y'])
						x_train.append(position['z'])
						x_train.append(orientation['x'])
						x_train.append(orientation['y'])
						x_train.append(orientation['z'])
						x_train.append(orientation['w'])
					
					frameTrain.append(x_train)
			
				loadedData.append(frameTrain)
				loadedAnswer.append(appendable)


	data = np.array(loadedData)
	answers = np.array(loadedAnswer)

	return data, answers



def jsonLoad(file):
	if os.path.isfile(file) is False:

		raise Exception("the filepath does not exist")

	base = open(file, 'r')
	loaded = json.load(base)
	frameTrain = []
	for frame in loaded['frames']:
		
		x_train = []
		rightHand = frame['right']
		#x_train.append(frame['timestamp'])
		for joint in skeleton:
			
			position = rightHand[joint]['position']
			orientation = rightHand[joint]['orientation']
				
			x_train.append(position['x'])
			x_train.append(position['y'])
			x_train.append(position['z'])
			x_train.append(orientation['x'])
			x_train.append(orientation['y'])
			x_train.append(orientation['z'])
			x_train.append(orientation['w'])
				
		frameTrain.append(x_train)
		
	folder = os.path.basename(os.path.dirname(file))

	if folder == "flick":

		loadedAnswer = 0

	elif folder == "fist":

		loadedAnswer = 1

	elif folder == "like":

		loadedAnswer = 2

	elif folder == "ring":

		loadedAnswer = 3

	elif folder == "tester":

		loadedAnswer = -1

	elif folder == "tester2":

		loadedAnswer = -1

	else:

		raise Exception("this folder " + folder + " has not been accounted for or should not exist")

	return frameTrain, loadedAnswer

