import pytest
import numpy as np
import cv2
from delaunay2 import get_color, DelaunayDiagram


@pytest.mark.parametrize(("a1,a2,a3,b,g,r"), [
    (120,100,150,0,0,255), #true
    (0,0,0,255.0, 255.0, 255),
    (12.5,24,60,94.16666666666669, 94.16666666666669, 255),
    (50,20,20,105.0,105.0,255), 
    (-20,-20,-20,255, 155.0, 155.0),
    
])

def test_get_color(a1,a2,a3, b, g, r):
    ans = get_color(a1,a2,a3)
    assert ans == (b, g, r)

def test_errored_get_color():
    with pytest.raises(Exception) as e:
        _ = get_color('','','')
    str(e.value) == "入力がありません"

height = 300
width = 300
@pytest.fixture
def make_img():
    img = np.full((height,width, 3), 255, np.uint8)
    return img

@pytest.fixture
def make_subdiv_array():
    rect = (0, 0, height, width)
    subdiv = cv2.Subdiv2D(rect)
    np.random.seed(0)
    array = np.zeros((width,height))
    pts = np.random.randint(0, 100, (50, 3))
    for p in pts:
        subdiv.insert((int(p[0]), int(p[1])))
        array[int(p[0])][int(p[1])] = p[2]
    return (subdiv,array)


def test_DelaunayDiagram(make_img,make_subdiv_array):
    subdiv = make_subdiv_array[0]
    array = make_subdiv_array[1]
    assert DelaunayDiagram(make_img,subdiv,array) == None
    
def test_error_DelaunayDiagram():
    with pytest.raises(Exception):
        DelaunayDiagram('','','')
    #assert MyError in str(excinfo)

