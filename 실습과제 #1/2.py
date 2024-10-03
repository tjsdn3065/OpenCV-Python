"""
2. 첨부된 logo.jpg 영상을 읽어서 R, G, B 채널로 각각 분리(split)한 후에 R채널에 100을 뺴고,
   G 채널은 0.5만큼 배수를 하고, B 채널은 반전(255-B)를 한 후에 다시 RGB영상으로 합쳐서(merge) 화면에 표시하시오.

"""

import numpy as np
import cv2

image=cv2.imread("logo.jpg",cv2.IMREAD_COLOR)       # 영상 읽기
if image is None:
    raise Exception("영상 읽기 에러 발생")

split_bgr=cv2.split(image)                          # 채널 분리

ch_R=cv2.subtract(split_bgr[2],100)             # R 채널 100빼기
ch_G=(split_bgr[1] * 0.5).astype(np.uint8)          # G 채널 0.5배
ch_B=cv2.subtract(255,split_bgr[0])             # B 채널 반전

new_image=[ch_B,ch_G,ch_R]

merge_bgr=cv2.merge(new_image)                      # 다시 합치기

cv2.imshow("image",merge_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()