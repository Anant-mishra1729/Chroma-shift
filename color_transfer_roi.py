from color_transfer import color_transfer
import cv2
import numpy as np

s = cv2.imread("morning.jpg")
t = cv2.imread("sunset.jpg")

# # Selecting ROI instead of complete image
s = s[0:500,200:700]

res = np.hstack(
    [
        cv2.resize(s, (512, 512)),
        cv2.resize(t, (512, 512)),
        cv2.resize(color_transfer(s, t), (512, 512)),
    ]
)

cv2.imshow("Output", res)
cv2.waitKey(0)
