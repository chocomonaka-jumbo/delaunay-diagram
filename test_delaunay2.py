#pytest --cov=. --cov-report=html
#pytest --cov -v test_delaunay2.py
from webbrowser import get
import pytest
import numpy as np
import pandas as pd
import cv2
import csv
from delaunay2 import get_color, DelaunayDiagram, openfile, main


@pytest.mark.parametrize(("a1,a2,a3,b,g,r"), [
    (120,100,150,0,0,255), #true
    (0,0,0,255.0, 255.0, 255),
    (12.5,24,60,94.16666666666669, 94.16666666666669, 255),
    (50,20,20,105.0,105.0,255), 
    (-20,-20,-20,255, 155.0, 155.0),
])
#正常に動作
def test_get_color(a1,a2,a3, b, g, r):
    ans = get_color(a1,a2,a3)
    assert ans == (b, g, r)

#エラー発生させる
def test_error_get_color():
    a1 = 50
    a2 = 30
    with pytest.raises(Exception):
        get_color()
    with pytest.raises(Exception):
        get_color(a1)
    with pytest.raises(Exception):
        get_color(a1,a2)
    
    



height = 100
width = 100
@pytest.fixture
def make_img():
    img = np.full((height,width, 3), 255, np.uint8)
    return img

@pytest.fixture
def make_pts():
    rect = (0, 0, height, width)
    subdiv = cv2.Subdiv2D(rect)
    np.random.seed(0)
    array = np.zeros((width,height))
    pts = np.random.randint(0, 100, (50, 3))
    for p in pts:
        subdiv.insert((int(p[0]), int(p[1])))
        array[int(p[0])][int(p[1])] = p[2]
    return (subdiv,array)

@pytest.fixture
def make_img2():
    img = np.full((50,50, 3), 255, np.uint8)
    return img


def test_DelaunayDiagram(make_img,make_pts,make_img2):
    subdiv = make_pts[0]
    array = make_pts[1]
    assert DelaunayDiagram(make_img,subdiv,array) == None
    assert DelaunayDiagram(make_img2,subdiv,array) == None



@pytest.fixture
def make_error_pts():
    rect = (0, 0, height, width)
    subdiv = cv2.Subdiv2D(rect)
    np.random.seed(0)
    array = np.zeros((width,height))
    pts = np.random.randint(0, 100, (50, 3))
    for p in pts:
        subdiv.insert((int(p[0]), int(p[1])))
        array[int(p[0])][int(p[1])] = p[2]
    return (subdiv,array)

def test_error_DelaunayDiagram(make_error_pts):
    subdiv = make_error_pts[0]
    array = make_error_pts[1]
    with pytest.raises(Exception):
        DelaunayDiagram(array)

def test_error_DelaunayDiagram2():
    with pytest.raises(Exception):
        DelaunayDiagram('','','')
    

@pytest.fixture
def write_file():
    header = ['x','y','temp']
    pts = np.random.randint(0, 100, (50, 3))
    with open('sample.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(pts)
        f.close()
    return pts


def test_openfile(write_file):
    
    assert (openfile('sample.csv') == write_file).any()

def test_error_openfile():
    with pytest.raises(Exception):
        openfile("")


