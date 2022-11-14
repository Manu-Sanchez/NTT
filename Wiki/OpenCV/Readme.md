# OpenCV

"""
Versión: 0.1
Last-Update: 2022-11-14
Author: Manuel Sánchez Mascarell
"""
## Working with images
	
### 	Read and Display an Image
	#Set img PATH 
	path = <img_path>
	
	#Read the image
	img = cv2.imread(path)
	
	#Display the image
	cv2.imshow(<frame_name>, img)

	#Stop displaying the image
	while True:
		if cv2.waitKey(1) == 0xFF & ord('q'): 
			break
	
	cv2.destroyAllWindows()

### 	Change color workspace
	c2.cvtColor(img, cv2.<color_code>)
	
	#By default cv2 works in BGR colorspace and matplotlib in RGB
	cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

###	Flip the image
	cv2.flip(img, <flip_code>)

	<flip_code>::= [0 | 1 | -1]
		|_ 0: flips horizonal
		|_ 1: flips vertical
		|_ -1: flips both
