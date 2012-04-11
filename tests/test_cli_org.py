#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.org import Org
from commands.base import Base

xfail = pytest.mark.xfail

class TestOrg:
    
    def test_org_list(self):
        org = Org()       
        out, err = org.org_list()
        Assert.equal(err, None)
        
    def test_org_create(self):
        org = Org()
        #base = Base()
        new_org_name = "Org%s" % Base.random_string()
        out,err = org.org_create(new_org_name)
        Assert.equal(err,None)


    def test_org_info(self):
        org = Org()
	#base = Base()
        new_org_name = "Org%s" % Base.random_string()
	out,err = org.org_info(new_org_name)
	Assert.equal(err,None)


    def test_org_update(self):
        org = Org()
	#base = Base()
        new_org_name = "Org%s" % Base.random_string()
        out,err = org.org_update(new_org_name)
        Assert.equal(err,None)


    def test_org_delete(self):
        org=Org()
	#base = Base()
        new_org_name = "Org%s" % Base.random_string()
        out,err = org.org_delete(new_org_name)
        Assert.equal(err,None)


    def test_org_subscriptions(self):
        org=Org()
        #base = Base()
        new_org_name = "Org%s" % Base.random_string()
        out,err = org.org_subscriptions(new_org_name)
        Assert.equal(err,None)

