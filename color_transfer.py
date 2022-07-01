import cv2
import numpy as np
import argparse

def mean_std(image):
	# Splitting image into channels
	c1, c2, c3 = cv2.split(image)

	# Calculating Mean and Standard Deviation of each channel
	c1mean, c1std = c1.mean(), c1.std()
	c2mean, c2std = c2.mean(), c2.std()
	c3mean, c3std = c3.mean(), c3.std()
	return (c1mean, c2mean, c3mean, c1std, c2std, c3std)


def color_transfer(source, target):
	# Converting image from RGB to Lαβ color space
	source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype(np.float32)
	target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype(np.float32)

	# Calculating Mean and Standard Deviation of source and target images
	(lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = mean_std(source)
	(lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = mean_std(target)

	# Subtracting means of target image from target channels
	l, a, b = cv2.split(target)
	l -= lMeanTar
	a -= aMeanTar
	b -= bMeanTar

	# Scaling target channels
	# By ratio of (stdTarget/stdSource)*(Target Channel)
	l *= lStdTar / lStdSrc
	a *= aStdTar / aStdSrc
	b *= bStdTar / bStdSrc

	# Adding Source Mean to Resulting channels
	l += lMeanSrc
	a += aMeanSrc
	b += bMeanSrc

	# Clip values which fall outside range[0,255]
	l = np.clip(l, 0, 255)
	a = np.clip(a, 0, 255)
	b = np.clip(b, 0, 255)

	# Merge channels together -> Convert to RGB color space
	result = cv2.merge([l, a, b])
	result = cv2.cvtColor(result.astype(np.uint8), cv2.COLOR_LAB2BGR)

	return result

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--source","-s",required=True,help="Path of image from whose color texture is being used")
	parser.add_argument("--target","-t",required=True,help="Path of image on color texture is being applied")
	args = vars(parser.parse_args())
	source = cv2.imread(args["source"])
	target = cv2.imread(args["target"])
	result = color_transfer(source,target)
	cv2.imwrite("result.jpg",result)
