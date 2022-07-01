import cv2
import numpy as np


def image_stats(image):
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
    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

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
	s = cv2.imread("morning.jpg")
	t = cv2.imread("sunset.jpg")

	res = np.hstack(
		[
			cv2.resize(s, (512, 512)),
			cv2.resize(t, (512, 512)),
			cv2.resize(color_transfer(s, t), (512, 512)),
		]
	)
	cv2.imshow("Output", res)
	cv2.waitKey(0)
