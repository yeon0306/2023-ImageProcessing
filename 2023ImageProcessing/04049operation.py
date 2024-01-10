import cv2
import numpy as np
img1 = cv2.imread('./img/wing_wall.jpg')
img2 = cv2.imread('./img/yate.jpg')
img3 = img1 + img2
img4 = cv2.add(img1, img2)
img5 = img1 * 0.3 + img2 * 0.7
img5 = img5.astype(np.uint8)

cv2.imshow('wing', img1)
cv2.imshow('yate', img2)
cv2.imshow('add', img3)
cv2.imshow('cvadd', img4)
cv2.imshow('add11', img5)

cv2.waitKey()
cv2.destroyAllWindows()

win_name = 'Alpha blending'     # 창 이름
trackbar_name = 'fade'          # 트렉바 이름

# ---① 트렉바 이벤트 핸들러 함수
def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
    cv2.imshow(win_name, dst)


# # ---② 합성 영상 읽기
# img1 = cv2.imread('./img/man_face.jpg')
# img2 = cv2.imread('./img/lion_face.jpg')

# ---③ 이미지 표시 및 트렉바 붙이기
cv2.imshow(win_name, img1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()