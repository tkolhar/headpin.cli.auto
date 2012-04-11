#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.client import Client
from commands.base import Base

xfail = pytest.mark.xfail

class TestClient:
    
    def test_client_remember(self):
        client = Client()
	base = Base()
 	optionname  = "org"
	value = "Org%s" % base.random_string()
        out, err = client.client_remember(optionname,value)
        Assert.equal(err,None)

    def test_client_forget(self):
        client = Client()
        base = Base()
        optionname  = "org"
        value = "Org%s" % base.random_string()
        out, err = client.client_forget(optionname,value)
        Assert.equal(err,None)

    def test_client_saved_options(self):
        client = Client()
        out, err = client.client_saved_options()
        Assert.equal(err,None)


    def test_client_forget(self):
        client = Client()
        base = Base()
        optionname  = "org"
        value = "Org%s" % base.random_string()
        out, err = client.client_forget(optionname,value)
        Assert.equal(err,None)

