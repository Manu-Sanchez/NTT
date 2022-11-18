import cv2
import sys

#dev_code = input("Set dev code")
dev = cv2.VideoCapture("bus/usb/)



if not dev.isOpened():
	print("Error with the camera")
	sys.exit()

while True:

	ret, frame = dev.read()
	cv2.imshow("Cam", frame)

	if cv2.waitKey(1) == 27:
		break

dev.release()
cv2.destroyAllWindows()
