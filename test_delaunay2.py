import pytest
from delaunay2 import get_color


@pytest.mark.parametrize(('a1', 'a2', 'a3', 'b','g','r'), [
    (120,100,150,0,0,255), #true
    (0,0,0,0,0,0),#false
    (-10,2,-15,0,0,0),#false
    (12.5,24,60,94.16666666666669, 94.16666666666669, 255),#true
    ('a',20,100,23,10,0)#false
])
def test_get_color(a1,a2,a3, b, g, r):
    assert get_color(a1,a2,a3) == (b, g, r)
