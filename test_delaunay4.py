import pytest

from delaunay3 import hsv_to_rgb
from delaunay3 import get_ave
from delaunay3 import get_color

@pytest.mark.parametrize(('h', 's', 'v', 'b','g','r'), [
    (129,160,255,118,255,95),
    (283,179,118,118,35,95),
    (203,255,57,57,35,0),
    (240,255,147,147,0,0),
    (-20,100,100,0,0,0),#指定した範囲外
    (300,300,300,0,0,0),#指定した範囲外
    (144.0,255.0,255.0,101,255,0),#実数を入力

])
def test_hsv_to_rgb(h, s, v, b, g, r):
    assert hsv_to_rgb(h, s, v) == (b, g, r)

@pytest.mark.parametrize(('array','inner_pts','ave','ave_max','ave_min'), [
    
])
def test_get_ave(array,inner_pts,ave,ave_max,ave_min):
    assert get_ave(array,inner_pts) == (ave, ave_max, ave_min)
    

@pytest.mark.parametrize(('a1','a2','a3','ave','ave_max','ave_min','b','g','r'), [
    (100,100,100,110,150,90,255,179,179),
    (100,100,100,100,100,100,255,215,215),#ave_max==ave_min
    (150,120,100,130,180,100,255,152,152),
    (100,110,100,150,200,100,255,207,207),
    (100.0,110.0,100.0,150,200,100,255,207,207)#実数
])
def test_get_color(a1,a2,a3,ave,ave_max,ave_min,b,g,r):
    assert get_color(a1,a2,a3,ave,ave_max,ave_min) == (b,g,r)
