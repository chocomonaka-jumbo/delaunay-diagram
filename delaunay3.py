#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2
import numpy as np
import math
import colorsys


# In[11]:


#ランダムで座標と値を発生
#本番はリストで受け取るので、この関数は不要
def getRandom2DPoints(width, height, n):
    """
    with open('sample.csv','r') as f:
        reader = csv.reader(f)
        pts = np.zeros((50,3))
        i = 0
        for line in reader:
            if(i>0):
                pts[i-1][0]=line[0]
                pts[i-1][1]=line[1]
                pts[i-1][2]=line[2]
            i=i+1
    """
    
    x = np.random.randint(0, width, n)
    y = np.random.randint(0, height, n)
    temp = np.random.randint(0, 45, n)
    
    pts = np.stack([x, y, temp], axis=1) 
    
    return    pts


# In[12]:


def hsv_to_rgb(h, s, v):
    #hsv値からrgb値に変換
    #bgr = cv2.cvtColor(np.array([[[h,s,v]]], dtype=np.uint8), cv2.COLOR_HSV2BGR)[0][0]
    
    max = v
    min = max - ((s/255)*max)
    
    if h >= 0 and h < 60:
        b = min
        g = (h/60)*(max-min) + min
        r = max
    elif h >= 60 and h < 120:
        b = min
        g = max
        r = ((120-h)/60)*(max-min)+min
    elif h >= 120 and h < 180:
        b = ((h-120)/60)*(max-min)+min
        g = max
        r  = min
    elif h >= 180 and h < 240:
        b = max
        g = ((240-h)/60)*(max-min)+min
        r  = min
    elif h >= 240 and h < 300:
        b = max
        g = min
        r  = ((h-240)/60)*(max-min)+min
    else:
        b = ((360-h)/60)*(max-min)+min
        g = min
        r = max
    
    b = int(b)
    g = int(g)
    r = int(r)
    
    return (b,g,r)


# In[13]:


def get_color(a1,a2,a3,ave,ave_max,ave_min):
    
    #3点の平均値
    ave_3pts = (a1+a2+a3)/3
    
    if ave_3pts > ave:
        h = 0
    else:
        h = 240
    #正規化
    n = (ave_3pts-ave_max)/(ave_max-ave_min)
    #s値を40から225の間の値に変換
    s = n*(255-40) + 255
    v = 255
    bgr = hsv_to_rgb(h,s,v)
    
    return(bgr[0], bgr[1], bgr[2])


# In[14]:


def get_ave(array,inner_pts):
    # 3点の平均値の平均値と標準偏差
    list = []
    for i in range(len(inner_pts)):
        pts1 = array[(int)(inner_pts[i][0][0])][(int)(inner_pts[i][0][1])]
        pts2 = array[(int)(inner_pts[i][1][0])][(int)(inner_pts[i][1][1])]
        pts3 = array[(int)(inner_pts[i][2][0])][(int)(inner_pts[i][2][1])]
        ave_3pts = (pts1 + pts2 + pts3)/3
        list.append(ave_3pts)
    ave = np.mean(list)
    ave_max = np.amax(list)
    ave_min = np.amin(list)
    return (ave,ave_max,ave_min)


# In[15]:


def DelaunayDiagram(imgd, subdiv,array):
    height, width = imgd.shape[:2]

    # ドロネーの三角形
    triangles = subdiv.getTriangleList()
    pols = triangles.reshape(-1, 3, 2)
    inner_pts = np.empty((0, 3, 2))
    
    for pa in pols:
        # フレーム外の点は除外
        cnt = 0
        for p in pa:
            if p[0] < 0 or width <= p[0] :
                break
            if p[1] < 0 or height <= p[1] :
                break
            cnt += 1
        # フレーム内の点は有効
        if cnt == 3:
            inner_pts = np.append(inner_pts, [pa], axis=0)
    
    #rgb値を格納する配列を作成
    color_list = np.zeros((len(inner_pts),3))
    
    ave = get_ave(array,inner_pts)[0]
    ave_max = get_ave(array,inner_pts)[1]
    ave_min = get_ave(array,inner_pts)[2]
    
    #3値を渡して色を設定
    for i in range(len(inner_pts)):
        pts1 = array[(int)(inner_pts[i][0][0])][(int)(inner_pts[i][0][1])]
        pts2 = array[(int)(inner_pts[i][1][0])][(int)(inner_pts[i][1][1])]
        pts3 = array[(int)(inner_pts[i][2][0])][(int)(inner_pts[i][2][1])]
        color_list[i]=get_color(pts1,pts2,pts3,ave,ave_max,ave_min)
    
        
    #図形の描画
    for i in range(len(inner_pts)):
        #三角形の描画
        cv2.fillPoly(imgd, [inner_pts[i].astype(int)], color_list[i], 1)
        #三角形の辺の描画
        cv2.line(imgd,(inner_pts[i][0][0].astype(int),inner_pts[i][0][1].astype(int)),(inner_pts[i][1][0].astype(int),inner_pts[i][1][1].astype(int)),(0,0,0))
        cv2.line(imgd,(inner_pts[i][1][0].astype(int),inner_pts[i][1][1].astype(int)),(inner_pts[i][2][0].astype(int),inner_pts[i][2][1].astype(int)),(0,0,0))
        cv2.line(imgd,(inner_pts[i][2][0].astype(int),inner_pts[i][2][1].astype(int)),(inner_pts[i][0][0].astype(int),inner_pts[i][0][1].astype(int)),(0,0,0))


# In[16]:


def main():
    width = 320
    height = 240
    
    #点の生成
    pts = getRandom2DPoints(width,height,50)
    
    #白紙を作る
    img = np.full((height, width, 3), 255, np.uint8)
    
    rect = (0, 0, width, height)
    subdiv = cv2.Subdiv2D(rect)

    #(x1,y1,a1)の時、array[x1][y1]=a1とする
    array = np.zeros((width,height))
    
    for p in pts:
        subdiv.insert((int(p[0]), int(p[1])))
        array[p[0]][p[1]] = p[2]
        
    DelaunayDiagram(img, subdiv,array)

    for p in pts:
        cv2.circle(img, (p[0],p[1]), 4, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
   
    cv2.imwrite('test2.png', img)


# In[17]:


if __name__ == '__main__':
    main()


# In[ ]:




