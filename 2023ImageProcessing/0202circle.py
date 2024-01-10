import cv2
import numpy as np
img = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.circle(img, (150, 150),100,(255,0,0), -1)

cv2.ellipse(img, (150, 300), (50, 50), -1)
cv2.ellipse(img, (150, 150),10,(255,0,0), -1)

cv2.imshow("lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




