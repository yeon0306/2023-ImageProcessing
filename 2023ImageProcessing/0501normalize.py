# import cv2
#
# img = cv2.imread('./img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)
# img_norm =cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
#
# cv2.imshow("", img)
# cv2.imshow(" ", img_norm)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =========================================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the images
img = cv2.imread('./img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)
img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# Calculate histograms
hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_img_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 256])

# Display the histograms using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(hist_img, color='blue')
plt.title('Histogram - Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.plot(hist_img_norm, color='blue')
plt.title('Histogram - Normalized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

