# coding: UTF-8
import cv2
import numpy as np
import math
import colorsys


#%%
#ランダムで座標と値を発生
def getRandom2DPoints(width, height, n):
    x = np.random.randint(0, width, n)
    y = np.random.randint(0, height, n)
    temp = np.random.randint(-10, 45, n)

    pts = np.stack([x, y, temp], axis=1) 
    return    pts

#rgb値求める
def get_color(a1,a2,a3):
    #平均値を求める
    ave = (a1+a2+a3)/3
    r = ave*5
    g = 0
    b = (50-ave)*5
    return(r,g,b)



#%%
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
    
    #3値を渡して色を設定
    for i in range(len(inner_pts)):
        color_list[i]=get_color(array[(int)(inner_pts[i][0][0])][(int)(inner_pts[i][0][1])],array[(int)(inner_pts[i][1][0])][(int)(inner_pts[i][1][1])],array[(int)(inner_pts[i][2][0])][(int)(inner_pts[i][2][1])])
    #図形の描画
    for i in range(len(inner_pts)):
        #三角形の描画
        cv2.fillPoly(imgd, [inner_pts[i].astype(int)], color_list[i], 1)
        #三角形の辺の描画
        cv2.line(imgd,(inner_pts[i][0][0].astype(int),inner_pts[i][0][1].astype(int)),(inner_pts[i][1][0].astype(int),inner_pts[i][1][1].astype(int)),(0,0,0))
        cv2.line(imgd,(inner_pts[i][1][0].astype(int),inner_pts[i][1][1].astype(int)),(inner_pts[i][2][0].astype(int),inner_pts[i][2][1].astype(int)),(0,0,0))
        cv2.line(imgd,(inner_pts[i][2][0].astype(int),inner_pts[i][2][1].astype(int)),(inner_pts[i][0][0].astype(int),inner_pts[i][0][1].astype(int)),(0,0,0))

#%%
def main():
    height = 240
    width = 320
    
    #点の生成
    pts = getRandom2DPoints(width,height,50)
    
    #白紙を作る
    img = np.full((height, width, 3), 255, np.uint8)
    
    rect = (0, 0, width, height)
    subdiv = cv2.Subdiv2D(rect)
    print(subdiv)

    #(x1,y1,a1)の時、array[x1][y1]=a1とする
    array = np.zeros((width,height))
    
    for p in pts:
        subdiv.insert((int(p[0]), int(p[1])))
        array[p[0]][p[1]] = p[2]
        
    DelaunayDiagram(img, subdiv, array)
    subdiv

    for p in pts:
        
        cv2.circle(img, (p[0],p[1]), 4, (0,0,0), thickness=-1, lineType=cv2.LINE_AA)

    cv2.imwrite('test2.png', img)

if __name__ == '__main__':
    main()
# %%
