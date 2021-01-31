from os import path 
from glob import glob 

import cv2 

import numpy as np 
import operator as op 
import itertools as it, functools as ft 

import argparse 

def create_screen(screen_name, width, height):
	cv2.namedWindow(screen_name, cv2.WINDOW_NORMAL)  # WINDOW_[NORMAL, AUTOSIZE]
	cv2.resizeWindow(screen_name, width	, height)

def read_image(image_path):
	return cv2.imread(image_path, cv2.IMREAD_COLOR)  # IMREAD_[COLOR, UNCHANGED, GRAYSCALE]

def display(target_screen, image):
	cv2.imshow(target_screen, image)


def remove_noise(contours):
	biggest_contour = max(contours, key=cv2.contourArea)
	biggest_area = cv2.contourArea(biggest_contour)
	return [cnt for cnt in contours if cv2.contourArea(cnt) / biggest_area > 0.1]

def read_video(video_path):
	main_screen = 'main screen'
	mask_screen = 'mask screen'
	create_screen(main_screen, 640, 480)
	create_screen(mask_screen, 640, 480)


	capture = cv2.VideoCapture(video_path)
	subtractor = cv2.createBackgroundSubtractorKNN() 

	keep_grabbing = True 
	while keep_grabbing:
		key_code = cv2.waitKey(25) & 0xFF  # 25ms 
		keep_grabbing = key_code != 27  # keep processing until the user hit the [echap] button
		read_status, frame = capture.read()  # read frame by frame from video_path 
		if read_status: 
			mask = subtractor.apply(frame)
			contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
			if len(contours) > 0: # some contours were found   # BGR 
				contours = remove_noise(contours)  # filter not valid contours 
				print('Number of persons : ', len(contours))
				cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)
				for cnt in contours:
					x, y, w, h = cv2.boundingRect(cnt)
					cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

			cv2.imshow(main_screen, frame)
			cv2.imshow(mask_screen, mask) 

	cv2.destroyAllWindows()


if __name__ == '__main__':
	print(' ... [procesing module] ... ')
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--source', help='path to video source data', required=True)
	
	vars_map = vars(parser.parse_args())
	read_video(vars_map['source'])

	
