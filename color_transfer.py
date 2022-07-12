import cv2
import numpy as np
import argparse
from os.path import basename

def resultName(source,target):
	s = basename(source).split(".")[0] + "_"
	t = basename(target).split(".")[0] + ".jpg"
	return "result\\" + s + t

def color_transfer(source, target):
	source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype(np.float32)
	target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype(np.float32)
	srcMean, srcStd = cv2.meanStdDev(source)
	targetMean, targetStd = cv2.meanStdDev(target)
	res = []
	for i, channel in enumerate(cv2.split(target)):
		channel -= targetMean[i]
		channel *= srcStd[i] / targetStd[i]
		channel += srcMean[i]
		res.append(np.clip(channel, 0, 255).astype("uint8"))
	result = cv2.merge(res)
	return cv2.cvtColor(result, cv2.COLOR_LAB2BGR)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--source",
		"-s",
		required=True,
		help="Path of image from whose color texture is being used",
	)
	parser.add_argument(
		"--target",
		"-t",
		required=True,
		help="Path of image on color texture is being applied",
	)
	parser.add_argument(
		"--result", "-r", default="result\\result.jpg", help="Path of resulting image"
	)
	args = vars(parser.parse_args())

	source = cv2.imread(args["source"])
	target = cv2.imread(args["target"])
	result = color_transfer(source, target)
	cv2.imwrite(resultName(args["source"],args["target"]), result)
