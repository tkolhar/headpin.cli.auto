#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.ping import Ping

xfail = pytest.mark.xfail

class TestPing:
    
    def test_ping(self):
        out, err = Ping.ping_status()
        Assert.equal(err, None)
        
