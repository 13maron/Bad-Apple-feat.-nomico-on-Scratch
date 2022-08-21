# coding: utf-8 (maybe)

import cv2
import os

def conv(path="Bad Apple!!.mp4", frames=6571):
	capt = cv2.VideoCapture(path)
	if capt.isOpened():
		os.makedirs("./images/", exist_ok=True)
		digit = len(frames)
		for i in range(digit):
			suc, imgArray = capt.read()
			cv2.imwrite('{}{}{}'.format("./images/", str(i).zfill(digit), ".jpg"), imgArray)
