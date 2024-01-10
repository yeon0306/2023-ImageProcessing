# # import cv2
# # import numpy as np
# #
# # img = np.full((500, 1000, 3), 255, dtype=np.uint8)
# #
# # cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,0))
# # cv2.putText(img, "아름다운 강산-최은주", (50, 200), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0,0))
# #
# # cv2.imshow('draw text', img)
# # cv2.waitKey()
# # cv2.destroyAllWindows()
#
#
# # ==================================================================
#
#
#
# from PIL import ImageFont, ImageDraw, Image
# import numpy as np
# import cv2
#
# # 이미지 생성
# img = np.full((500, 1000, 3), 255, dtype=np.uint8)
#
# # OpenCV로 Plain 텍스트 표시
# cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
#
# # PIL 이미지로 변환
# image_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# draw = ImageDraw.Draw(image_pil)
#
# # 폰트 설정 (폰트 파일의 경로와 크기를 지정)
# font_path = r"C:\Users\AI-13\Downloads\maruburi\TTF\MaruBuri-ExtraLight.ttf"
# font = ImageFont.truetype(font_path, 30)
#
# # 텍스트 그리기 (위치, 내용, 폰트, 색상을 지정)
# draw.text((50, 200), "아름다운 강산-최은주", font=font, fill=(255, 255, 255, 0))
#
# # PIL 이미지를 OpenCV 형태로 변환
# img = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
#
# # 이미지 출력
# cv2.imshow('draw text', img)
# cv2.waitKey()
# cv2.destroyAllWindows()
#








#
# from PIL import ImageFont, ImageDraw, Image
# import numpy as np
# import cv2
#
# # 이미지 생성
# img = np.full((500, 1000, 3), 255, dtype=np.uint8)
#
# # OpenCV로 Plain 텍스트 표시
# cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
#
# # PIL 이미지로 변환
# image_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# draw = ImageDraw.Draw(image_pil)
#
# # 폰트 설정 (폰트 파일의 경로와 크기를 지정)
# font_path = r"C:\Users\AI-13\Downloads\maruburi\TTF\MaruBuri-ExtraLight.ttf"
# font = ImageFont.truetype(font_path, 30)
#
# # 텍스트 그리기 (위치, 내용, 폰트, 색상을 지정)
# cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
# draw.text((50, 200), "아름다운 강산-최은주", font=font, fill=(255, 255, 255, 0))
#
# # PIL 이미지를 OpenCV 형태로 변환
# img = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
#
# # 이미지 출력
# cv2.imshow('draw text', img)
# cv2.waitKey()
# cv2.destroyAllWindows()
#





import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 이미지 생성
img = np.full((500, 1000, 3), 255, dtype=np.uint8)

# OpenCV로 Plain 텍스트 표시
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

# PIL 이미지로 변환
img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(img_pil)

# 폰트 설정 (폰트 파일의 경로와 크기를 지정)
font_path = r"C:\Users\AI-13\Downloads\maruburi\TTF\MaruBuri-ExtraLight.ttf"  # 여기에 실제 ttf 폰트 파일 경로를 입력해주세요.
font = ImageFont.truetype(font_path, 30)

# 텍스트 그리기 (위치, 내용, 폰트, 색상을 지정)
draw.text((50, 200), "아름다운 강산-최은주", font=font, fill='black')

# PIL 이미지를 OpenCV 형태로 변환
img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# 이미지 출력
cv2.imshow('draw text', img)
cv2.waitKey()
cv2.destroyAllWindows()



