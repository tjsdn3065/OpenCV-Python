"""
3. 첨부된 video_file.avi를 읽어서 각 프레임 별로 random한 ROI를 생성해서 ROI위치와 ROI 영역 내의 평균과 표준편차를 출력하시오.

"""

import numpy as np
import cv2

capture = cv2.VideoCapture("video_file.avi")
if not capture.isOpened():
    raise Exception("동영상 파일 개방 안됨")

frame_rate=capture.get(cv2.CAP_PROP_FPS)
delay=int(1000/frame_rate)

while True:
    ret,frame=capture.read()
    if not ret or cv2.waitKey(delay) >= 0:
        break

    y=np.random.randint(0,360)
    h = np.random.randint(0, 360-y)
    x=np.random.randint(0,640)
    w = np.random.randint(0, 640-x)
    
    roi = np.zeros(frame.shape[:2], np.uint8)
    roi[y:y+h, x:x+w] = 1

    mean,stddev=cv2.meanStdDev(frame,mask=roi)

    print("ROI 위치\n 좌상단: (%s, %s), 우하단: (%s, %s),  좌하단: (%s, %s), 우상단: (%s, %s)" % (x, y, x + w, y + h, x, y + h, x + w, y))
    print("[mean] =",mean.flatten())
    print("[stddev] =", stddev.flatten())

capture.release()