#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.org import Org
from commands.base import Base

xfail = pytest.mark.xfail

class TestOrg:
    
    def test_org_list(self):
        out, err = Org.org_list()
        Assert.equal(err, None)
        
    def test_org_create(self):
        new_org_name = "Org%s" % Base.random_string()
        out,err = Org.org_create(new_org_name)
        Assert.equal(err,None)


    def test_org_info(self):
        new_org_name = "Org%s" % Base.random_string()
	out,err = Org.org_info(new_org_name)
	Assert.equal(err,None)


    def test_org_update(self):
        new_org_name = "Org%s" % Base.random_string()
        out,err = Org.org_update(new_org_name)
        Assert.equal(err,None)


    def test_org_delete(self):
        new_org_name = "Org%s" % Base.random_string()
        out,err = Org.org_delete(new_org_name)
        Assert.equal(err,None)


    def test_org_subscriptions(self):
        new_org_name = "Org%s" % Base.random_string()
        out,err = Org.org_subscriptions(new_org_name)
        Assert.equal(err,None)

