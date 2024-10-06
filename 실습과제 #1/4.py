"""
4. 첨부된 abs_test1.jpg와 abs_test2.jpg를 읽어서 abs_test1.jpg는 x축 방향으로 뒤집고(flip)
   abs_test2.jpg는 x, y 축 방향으로 뒤집은(flip) 다음 두 영상을 0.4, 0.6의 비율로 합쳐서 출력하시오.

"""

import cv2

image1=cv2.imread("abs_test1.jpg",cv2.IMREAD_COLOR)
image2=cv2.imread("abs_test2.jpg",cv2.IMREAD_COLOR)

if image1 is None or image2 is None:
    raise Exception("영상 읽기 오류 발생")

x_image=cv2.flip(image1,0)
xy_image=cv2.flip(image2,-1)

new_image = cv2.addWeighted(x_image, 0.4, xy_image, 0.6, 0)

cv2.imshow("image1",image1)
cv2.imshow("image2",image2)
cv2.imshow("new_image",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()