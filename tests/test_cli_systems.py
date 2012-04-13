#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.system import System
from commands.base import Base

xfail = pytest.mark.xfail

class TestSystem:
    
    def test_system_list(self):
	new_org_name = "Org%s" % Base.random_string()
        out, err = System.system_list(new_org_name)
        Assert.equal(err, None)
        
    def test_system_unregister(self):
        new_org_name = "Org%s" % Base.random_string()
	new_sys_name = "Sys%s" % Base.random_string()
        out,err = System.system_unregister(new_org_name,new_sys_name)
        Assert.equal(err,None)


    def test_system_info(self):
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
	out,err = System.system_info(new_org_name,new_sys_name)
	Assert.equal(err,None)


    def test_system_update(self):
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
        out,err = System.system_update(new_org_name,new_sys_name)
        Assert.equal(err,None)


    def test_system_report(self):
        new_org_name = "Org%s" % Base.random_string()
        out,err = System.system_report(new_org_name)
        Assert.equal(err,None)


    def test_system_subscriptions(self):
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name  = "Sys%s" % Base.random_string()
        out,err = System.system_subscriptions(new_org_name,new_sys_name)
        Assert.equal(err,None)

    
    def test_system_facts(self):
        #system = System()
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
        out,err = System.system_facts(new_org_name,new_sys_name)
        Assert.equal(err,None)
      

    def test_system_subscribe(self):
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
	new_pool_id = "pool%s" % Base.random_string()
        out,err = System.system_facts(new_org_name,new_sys_name,new_pool_id)
        Assert.equal(err,None)

