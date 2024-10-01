"""
1. 마우스/키보드 인터페이스를 통한 그림판 만들기

- 그림판처럼 마우스를 이용해서 한 점에서 클릭을 하면 도형 그리기를 시작하고,
  마우스를 누른 상태로 움직이는 동안 해당 도형의 형태를 보여주다가 마우스를 놓으면 최종적으로 도형을 그려서 작업을 끝냄.
  새롭게 클릭을 하면 새로운 도형을 그려야 하며, 기존에 그린 도형은 남아 있어야 함.

- 도형은 기본적으로는 사각형(rectangle)을 하되,
  키보드 L을 누르면 직선(line), C를 누르면 원(circle), R을 누르면 사각형(rectangle)을 그리도록 함

- N을 누르면 모든 그린 그림을 지우고 빈 영상에서 시작하고, S를 누르면 현재 그린 그림을 figure.jpg로 저장함

"""

import numpy as np
import cv2
from math import sqrt

pt=(-1,-1)
diagram = None

def onMouse(event,x,y,flags,param):                                 # 마우스 콜백 함수
    global pt,image

    if event==cv2.EVENT_LBUTTONDOWN:                                # 마우스 왼쪽 버튼 누르기
        if pt[0] == -1:                                             # 처음 눌렀다면 시작 좌표 저장
            pt=(x,y)

    elif event==cv2.EVENT_MOUSEMOVE and pt[0] != -1:                # 누르고 있는 상태에서 도형 계속 그리기
        image_copy = image.copy()

        if diagram==ord('L'):
            cv2.line(image_copy,pt,(x,y),(255,0,0),3,cv2.LINE_AA)
        elif diagram==ord('C'):
            cv2.circle(image_copy,pt,int(sqrt((pt[0]-x)**2+(pt[1]-y)**2)),(0,255,0),3,cv2.LINE_AA)
        else:
            cv2.rectangle(image_copy, pt, (x, y), (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow(title1, image_copy)

    elif event==cv2.EVENT_LBUTTONUP:                                # 마우스 왼쪽 버튼을 뗐다면 도형 그리기 완성
        if diagram == ord('L'):
            cv2.line(image, pt, (x, y), (255, 0, 0), 3, cv2.LINE_AA)
        elif diagram == ord('C'):
            cv2.circle(image, pt, int(sqrt((pt[0] - x) ** 2 + (pt[1] - y) ** 2)), (0, 255, 0), 3, cv2.LINE_AA)
        else:
            cv2.rectangle(image, pt, (x, y), (0, 0, 255), 3, cv2.LINE_AA)
        pt=(-1,-1)                                                  # 시작 좌표 초기화
        cv2.imshow(title1, image)

def handle_key_event(key, image):
    if key == ord('R'):
        print("사각형")
        return ord('R')  # 사각형 그리기 모드
    elif key == ord('L'):
        print("선")
        return ord('L')  # 선 그리기 모드
    elif key == ord('C'):
        print("원")
        return ord('C')  # 원 그리기 모드
    elif key == ord('N'):
        print("초기화")
        return 'N'  # 화면 초기화
    elif key == ord('S'):
        print("저장")
        cv2.imwrite("figure.jpg", image)  # 이미지 저장
        return 'S'
    return None


image=np.full((480,640,3),255,np.uint8)                   # 초기 영상 생성
title1="assignment1"                                                 # 윈도우 이름
cv2.imshow(title1,image)                                             # 영상 보기
cv2.setMouseCallback(title1,onMouse)                                 # 마우스 콜백 함수 등록

try:
    while True:
        key = cv2.waitKey(100)
        if key == 27:
            break
        result = handle_key_event(key, image)
        if result == 'N':
            image = np.full((480, 640, 3), 255, np.uint8)
            cv2.imshow(title1, image)
        elif result is not None:
            diagram = result
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    cv2.destroyAllWindows()                                         # 열린 모든 윈도우 제거