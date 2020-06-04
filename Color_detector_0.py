import cv2
import numpy as np

def main():
	cap = cv2.VideoCapture(0)

	while True:
		_,frame = cap.read()

		frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		lower_yellow = np.array([30, 0, 0])
		upper_yellow = np.array([90, 255, 255])
		mask_yellow = cv2.inRange(frame_hsv, lower_yellow, upper_yellow)
		final_yellow = cv2.bitwise_and(frame, frame, mask = mask_yellow)

		lower_red = np.array([0, 150, 130])
		upper_red = np.array([15, 255, 255])
		mask_red = cv2.inRange(frame_hsv, lower_red, upper_red)
		final_red = cv2.bitwise_and(frame, frame, mask = mask_red)

		final_y_r = cv2.add(final_red, final_yellow)

		cv2.imshow("video_0", final_y_r)
		
		

		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

	cap.release()
	cv2.destroyAllWindows()





if __name__ == "__main__":
	main()
