import cv2
img_file = './img/colorblindpaper.jpg.png'
img = cv2.imread(img_file)
cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyWindow()

from PIL import Image
img = Image.open("img\colorblindpaper.jpg")
img.show()