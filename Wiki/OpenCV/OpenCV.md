# OpenCV

## OpenCV
	import cv2
	import matplotlib.pyplot as plt

### Read Images
	img = cv2.imread(<file_path>) #If <file_path> is wrong it will return None
	
	#You can specify the colorspace of the image 
	img = cv2.imread(<file_path>, <mode>)
	img_gray = cv2.imread(<file_path>, cv2.IMREAD_GRAYSCALE)

### Write Images
	cv2.imwrite(<file_path>, img)

### Show images - MatplotLib
Plot a single image.
	plt.plot(img)
	plt.show()

Create a figure with more than one image.
	fig, axis = plt.subplots(<rows>, <cols>, figsize=(<height>, <width>))
	
	axis[x][y].set_title(<title>)
	axis[x][y].plot(<plot>)	
	
	axis[x'][y'].set_title(<title>)
	axis[x'][y'].imshow(img)

	plt.show()

### Show images - Cv2
	cv2.imshow(<frame_title>, img)

You can wait a key pressed for closing the image
	while True:
		if cv2.waitKey(<seconds>) == 27:
			break
	
	cv2.destroyAllWindows()

## Resize images
cv2.resize(img, (height, width))

You can also mupltiply the height and width of an image to use aspect ratio
	myShape = img.shape
	ratio = 0.5
	
	cv2.resize(img, (myShape[0] * ratio, myShape[1] * ratio, myShape[2:])

## Draw Images
We're going to draw some figures in a image, for doing that we're going to use a black background.
	blk_bkg = np.zeros(shape=(512, 512, 3), dtype=np.int16) #We're going to use 3 channels for RGB

### Draw Rectangle
cv2.rectangle(img, pt1, pt2, color, thickness)
- img: base image where rectangle will be drawn
- pt1: top left point of the rectangle
- pt2: bottom right of the rectangle
- color: tuple of (R, G, B) with values from [0~255]
- thickness: Border thickness, (-1) for fill the rectangle

	cv2.rectangle(blk_bkg, pt1=(125, 125), pt2=(275, 350), color=(255, 255, 255), thickness=-1)

	
### Draw Circle
cv2.circle(img, center, radius, color, thickness)
- img: base image where rectangle will be drawn
- center: center of the circle
- radius: distance between center and edge
- color: tuple of (R, G, B) with values from [0~255]
- thickness: Border thickness, (-1) for fill the rectangle

	cv2.circle(blk_bkg, center=(255, 255), radius=20, color=(255, 255, 255), thickness=-1)

## Draw 
