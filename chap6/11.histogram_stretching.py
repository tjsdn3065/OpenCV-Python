import cv2
import numpy as np
from Common.utils import draw_histo

def search_value_idx(hist,bias=0):
    for i in range(hist.shape[0]):
        idx=np.abs(bias-i)
        if hist[idx]>0:
            return idx
    return -1

image = cv2.imread("images/hist_stretch.jpg",cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

bsize,ranges=[64],[0,256]
hist=cv2.calcHist([image],[0],None,bsize,ranges)

bin_width=ranges[1]/bsize[0]
low=search_value_idx(hist,0)*bin_width
high=search_value_idx(hist,bsize[0]-1)*bin_width

idx=np.arange(0,256)
idx=(idx-low)/(high-low)*255
idx[0:int(low)]=0
idx[int(high+1):]=255

dst=cv2.LUT(image,idx.astype("uint8"))

hist_dst=cv2.calcHist([dst],[0],None,bsize,ranges)
hist_img=draw_histo(hist,(200,360))
hist_dst_img=draw_histo(hist_dst,(200,360))

print("high_vlue = ",high)
print("low_vlue = ",low)
cv2.imshow("image",image)
cv2.imshow("hist_img",hist_img)
cv2.imshow("dst",dst)
cv2.imshow("hist_dst_img",hist_dst_img)
cv2.waitKey(0)