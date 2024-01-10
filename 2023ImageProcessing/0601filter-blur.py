import cv2
import numpy as np
img = cv2.imread('./img/gaussian_noise.jpg.jpg')
kernel = np.ones((5,5)) /25
blured = cv2.filter2D(img, -1, kernel)
cv2.imshow("origin", img)
cv2.imshow("blured", blured)
cv2.waitKey(0)
cv2.destroyAllWindows()


k1 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

#gaussian filter Library 사용
blur2 = cv2. GaussianBlur(img, (3, 3), 0)
cv2.imshow("origin", img)
cv2.imshow("blur2", blur2)
cv2.waitKey(0)
cv2.destroyAllWindows()