import cv2
import numpy as np

# 10도
img = cv2.imread('./img/children.jpg')
height, width = img.shape[0:2]
d10 = 10 * np.pi/180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), 0],
                  [np.sin(d10), np.cos(d10), 0]])
r10 = cv2.warpAffine(img, m10, (width, height))

cv2.imshow("", img)
cv2.imshow("r10", r10)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#70도
img = cv2.imread('./img/children.jpg')
height, width = img.shape[0:2]
d10 = 70 * np.pi/180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), height],
                  [np.sin(d10), np.cos(d10), 0]])
r10 = cv2.warpAffine(img, m10, (width, height))

cv2.imshow("", img)
cv2.imshow("r10", r10)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#90도
img = cv2.imread('./img/children.jpg')
height, width = img.shape[0:2]
d10 = 90 * np.pi/180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), height],
                  [np.sin(d10), np.cos(d10), 0]])
r10 = cv2.warpAffine(img, m10, (height, width))

cv2.imshow("", img)
cv2.imshow("r10", r10)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()

#180도

img = cv2.imread('./img/children.jpg')
height, width = img.shape[0:2]
d10 = 180 * np.pi / 180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), width],
                  [np.sin(d10), np.cos(d10), height]])
r10 = cv2.warpAffine(img, m10, (width, height))

cv2.imshow("", img)
cv2.imshow("r10", r10)
cv2.waitKey(0)
cv2.destroyAllWindows()

#

img = cv2.imread('./img/children.jpg')
height, width = img.shape[0:2]
d10 = 10 * np.pi / 180
fl1 = np.float32([[-1, 0, width-1],
                  [0,1,0]])
fl2 = np.float32([[-1, 0, width-1],
                  [0,1,height-1]])
r10 = cv2.warpAffine(img, fl1, (width, height))

cv2.imshow("", img)
cv2.imshow("flip", r10)
cv2.waitKey(0)
cv2.destroyAllWindows()

#

imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
dflipx = np.zeros_like(imgg)
for i in range (width):
        dflipx[:, i] = imgg[:, width-i-1]

cv2. imshow ("org", imgg)
cv2. imshow ("dflipx", dflipx)
cv2.waitKey(0)
cv2.destroyAllWindows()

#

imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
dflipy = np.zeros_like(imgg)
height = imgg.shape[0]

for i in range(height):
    dflipy[i, :] = imgg[height-i-1, :]

cv2.imshow("org", imgg)
cv2.imshow("dflipy", dflipy)
cv2.waitKey(0)
cv2.destroyAllWindows


#

import cv2
import numpy as np

imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
dflipxy = np.zeros_like(imgg)
height, width = imgg.shape

for i in range(height):
    for j in range(width):
        dflipxy[i, j] = imgg[height-i-1, width-j-1]

cv2.imshow("org", imgg)
cv2.imshow("dflipxy", dflipxy)

cv2.waitKey(0)
cv2.destroyAllWindows()


#


import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

imgg = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)
dflipxy = np.zeros_like(imgg)
height, width = imgg.shape

for i in range(height):
    for j in range(width):
        dflipxy[i, j] = imgg[height-i-1, width-j-1]

img_pil = Image.fromarray(dflipxy)
draw = ImageDraw.Draw(img_pil)

fontpath = "./img/MaruBuri-Bold.ttf"
font = ImageFont.truetype(fontpath, 20)

# fill을 (255, 255, 255, 0)에서 (255)로 변경합니다.
draw.text((50, 50), "최은주", font=font, fill=(255))

dflipxy = np.array(img_pil)

cv2.imshow("org", imgg)
cv2.imshow("dflipxy", dflipxy)

cv2.waitKey(0)
cv2.destroyAllWindows()

