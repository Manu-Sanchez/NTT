# Numpy basics for OpenCV

## Basics of Numpy
	import numpy as np
	
	myArray = [0, 1, 2]
	
	myArray = np.array(myArray) #Cast myArray to Numpy

	np.arrange(0, 10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	np.arrange(0, 10, 2) # [0, 2, 4, 6, 8]

	np.ones(shape = (2, 2)) # [ [1, 1], [1, 1] ]
	np.zeros(shape = (2, 2)) # [ [0, 0], [0, 0] ]
	
	np.random.seed(<random_seed>)
	np.random.randint(0, 100, 10) #From [0 ~ 100] take 10 numbers
	
### Get min/max value
	myArray.max() #Returns max value (2)
	myArray.argmax() #Returns position of the max value (2)

	myArray.min() #Returns min value (0)
	myArray.argmin() #Returns position of the min value (0)

### Array Indexing
	myArray.shape
	myArray.reshape(<new_shape>)

	myArray = [ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]
	myArray[<row>, <col>]
	myArray[0, 1] -> (1)
	myArray[0, :] -> [0, 1, 2]
	myArray[:, 1] -> [1, 4, 7]
	myArray[1:, 1:] -> [ [4, 5], [7, 8] ]
	myArray[0:1, :] -> [ [0, 1, 2] ]

	myArrayCopy = myArray.copy() # Using copy() will generate different memory reference
	
### Working with Images
	from PIL import Image
	
	img = Image(<file_path>)
	img = np.array(img)
	
	red_channel = img[:, :, 0]
	green_channel = img[:, :, 1]
	blue_channel = img[:, :, 2]

