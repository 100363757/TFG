import os
import random
import numpy as np

from jsonMuncher import jsonLoad


def choose():

	loadedData = []
	loadedAnswers = []
	

	for subdir, dirs, files in os.walk("./data"):
		for file in files:

			filepath = subdir + os.sep + file
			chosen = random.randint(0, 100)
			if chosen > 75:
				tempData, tempAnswer = jsonLoad(filepath)
				loadedData.append(tempData)
				loadedAnswers.append(tempAnswer)

	data = np.array(loadedData)
	answers = np.array(loadedAnswers)

	return data, answers


def test():

	loadedData = []
	loadedAnswers = []
	
	for subdir, dirs, files in os.walk("./data/tester2"):
		for file in files:

			filepath = subdir + os.sep + file
			tempData, tempAnswer = jsonLoad(filepath)
			loadedData.append(tempData)

	
	data = np.array(loadedData)

	return data