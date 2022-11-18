# Keras Basics

## Imports
	from sklearn.model_selection import train_test_split
	from sklearn.preprocessing import MinMaxScaler
	
	from keras.models import Sequential
	from keras.layers import dense 

	from numpy import genfromtxt
	import numpy as np


## Preprocess Data
These are the steps we're going to perform before training the machine learning model
* MinMaxScaler(feature_range=(0, 1), *, copy=True, clip=False)
	* feature_range: 	
	* *
	* copy: by default will create a copy instead of modifying inplace
	* clip
