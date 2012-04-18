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

    def test_client_remember_optionname_missing(self):
        value = "Org%s" % Base.random_string()
        out, err = Client.client_remember_optionname_missing(value)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --option option requires an argument\n")

    def test_client_remember_value_missing(self):
        optionname  = "org"
        out, err = Client.client_remember_value_missing(optionname)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --value option requires an argument\n")

    def test_client_forget(self):
        optionname  = "org"
        out, err = Client.client_forget(optionname)
        Assert.equal(err,None)

    def test_client_saved_options(self):
        out, err = Client.client_saved_options()
        Assert.equal(err,None)


    def test_client_forget_optionname_missing(self):
        out, err = Client.client_forget_optionname_missing()
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --option option requires an argument\n")
