import numpy as np,cv2

def print_rect(rects):
    print("-"*46)
    print("사각형 원소\t\t랜덤 사각형 정보\t 크기")
    print("-"*46)
    for i,(x,y,w,h,a) in enumerate(rects):
        print("rect[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" % (i,x,y,w,h,a))

rands=np.zeros((5,5),np.uint16)
starts=cv2.randn(rands[:,:2],100,50)
ends=cv2.randn(rands[:,2:-1],300,50)

sizes=cv2.absdiff(starts,ends)
areas=sizes[:,0]*sizes[:,1]
rects=rands.copy()
rects[:,2:-1]=sizes
rects[:,-1]=areas

idx=cv2.sortIdx(areas,cv2.SORT_EVERY_COLUMN).flatten()

print_rect(rects)
print_rect(rects[idx.astype("int")])