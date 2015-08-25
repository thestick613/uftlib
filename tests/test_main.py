# -*- coding: utf-8 -*-

from uftlib import UFTemplate


class TestMain(object):
    def test_simple_functionality(self):
        t = UFTemplate("x=0", "x+=1", "${x}")
        assert t.render() == '1'

    def test_render_many(self):
        t = UFTemplate('s = "x"', 's += "y"', "${s}")
        assert t.render_many(howmany=3) == ['xy', 'xyy', 'xyyy']

    def test_reset(self):
        t = UFTemplate("x=0", "x+=1", "${x}")
        assert t.render_many(howmany=4) == ['1', '2', '3', '4']
        assert t.render() == '5'
        t.reset()
        assert t.render_many(howmany=4) == ['1', '2', '3', '4']
