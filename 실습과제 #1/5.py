"""
5. equalize.jpg를 컬러로 읽고 R, G, B에 대한 히스토그램을 출력하시오.
   equalize.jpg를 흑백으로 읽고 히스토그램을 출력한 후에
   1) 히스토그램 스트레칭과 2) 히스토그램 평활화를 각각 수행한 후에 그 때의 결과 영상과 히스토그램을 각각 출력하시오.

"""

import cv2
import numpy as np

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = shape[1] / hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = max(int(round(gap)), 1)  # 최소 너비 1로 설정
        if h.size > 0:  # h가 스칼라가 아닌 배열일 경우
            h = h[0]
        cv2.rectangle(hist_img, (x, 0), (x + w, int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img, 0)

def search_value_idx(hist,bias=0):
    for i in range(hist.shape[0]):
        idx=np.abs(bias-i)
        if hist[idx]>0:
            return idx
    return -1

# 이미지 로드
image_color = cv2.imread("equalize.jpg", cv2.IMREAD_COLOR)
image_grayscale=cv2.imread("equalize.jpg", cv2.IMREAD_GRAYSCALE)
if image_color is None or image_grayscale is None:
    raise Exception("영상 파일 읽기 오류")

# 채널 분리
B, G, R = cv2.split(image_color)

bsize,ranges=[256],[0,256]
bin_width=ranges[1]/bsize[0]

# 히스토그램 평활화
equalize=cv2.equalizeHist(image_grayscale)

# 히스토그램 계산
R_hist = cv2.calcHist([R], [0], None, bsize, ranges)
G_hist = cv2.calcHist([G], [0], None, bsize, ranges)
B_hist = cv2.calcHist([B], [0], None, bsize, ranges)
hist=cv2.calcHist([image_grayscale],[0],None,bsize,ranges)
hist_equalize=cv2.calcHist([equalize],[0],None,bsize, ranges)

# 최저 화소값
low=search_value_idx(hist,0)*bin_width
# 최고 화소값
high=search_value_idx(hist,bsize[0]-1)*bin_width

idx=np.arange(0,256)
idx=(idx-low)/(high-low)*255
idx[0:int(low)]=0
idx[int(high+1):]=255
stretching=cv2.LUT(image_grayscale,idx.astype("uint8"))

# 히스토그램 재계산
hist_stretching=cv2.calcHist([stretching],[0],None,bsize, ranges)

# 히스토그램 이미지 생성
R_hist_img = draw_histo(R_hist)
G_hist_img = draw_histo(G_hist)
B_hist_img = draw_histo(B_hist)
hist_img=draw_histo(hist)
hist_stretching_img=draw_histo(hist_stretching)
hist_equalize_img=draw_histo(hist_equalize)

# 결과 출력
print("R : ",R_hist.flatten())
print("G : ",G_hist.flatten())
print("B : ",B_hist.flatten())

cv2.imshow("image_color", image_color)
cv2.imshow("image_grayscale", image_grayscale)
cv2.imshow("stretching", stretching)
cv2.imshow("equalize", equalize)
cv2.imshow("R_hist_img", R_hist_img)
cv2.imshow("G_hist_img", G_hist_img)
cv2.imshow("B_hist_img", B_hist_img)
cv2.imshow("hist_img", hist_img)
cv2.imshow("hist_stretching_img", hist_stretching_img)
cv2.imshow("hist_equalize_img", hist_equalize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
