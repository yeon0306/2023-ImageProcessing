import cv2
import numpy as np

img_face = cv2.imread('./img/man_face.jpg')
img_skull = cv2.imread('./img/skull.jpg')

height, width, _ = img_face.shape

middle = height // 2  # 세로 중간 지점을 찾습니다.

img = np.zeros_like(img_face)
img[:middle, :, :] = img_face[:middle, :, :].copy()
img[middle:, :, :] = img_skull[middle:, :, :].copy()

alpha_height_rate = 20  # 세로 반반으로 합칠 영역의 높이 비율
alpha_height = height * alpha_height_rate // 100
start = middle - alpha_height // 2
step = 100 / alpha_height

for i in range(alpha_height + 1):
    alpha = (100 - step * i) / 100
    beta = 1 - alpha
    img[start + i, :] = img_face[start + i, :] * alpha + img_skull[start + i, :] * beta

cv2.imshow('half skull', img)
cv2.waitKey(0)
cv2.destroyAllWindows()