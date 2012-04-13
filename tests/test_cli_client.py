#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.client import Client
from commands.base import Base

xfail = pytest.mark.xfail

class TestClient:
    
    def test_client_remember(self):
 	optionname  = "org"
	value = "Org%s" % Base.random_string()
        out, err = Client.client_remember(optionname,value)
        Assert.equal(err,None)

    def test_client_forget(self):
        optionname  = "org"
        value = "Org%s" % Base.random_string()
        out, err = Client.client_forget(optionname,value)
        Assert.equal(err,None)

    def test_client_saved_options(self):
        out, err = Client.client_saved_options()
        Assert.equal(err,None)


    def test_client_forget(self):
        optionname  = "org"
        value = "Org%s" % Base.random_string()
        out, err = Client.client_forget(optionname,value)
        Assert.equal(err,None)

