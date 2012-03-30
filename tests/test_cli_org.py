#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.org import Org

xfail = pytest.mark.xfail

class TestOrg:
    
    def test_org_list(self):
        org = Org()        
        out, err = org.org_list()
        Assert.equal(err, None)
        
    def test_org_create(self):
        org = Org()
        out,err = org.org_create("torg")
        Assert.equal(err,None)


    def test_org_info(self):
        org = Org()
	out,err = org.org_info("torg")
	Assert.equal(err,None)


    def test_org_update(self):
        org = Org()
        out,err = org.org_update("torg")
        Assert.equal(err,None)


    def test_org_delete(self):
        org=Org()
        out,err = org.org_delete("torg")
        Assert.equal(err,None)

