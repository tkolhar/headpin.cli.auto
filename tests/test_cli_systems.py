#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.system import System
from commands.base import Base

xfail = pytest.mark.xfail

class TestSystem:
    
    def test_system_list(self):
        system = System()       
	new_org_name = "Org%s" % Base.random_string()
        out, err = system.system_list(new_org_name)
        Assert.equal(err, None)
        
    def test_system_unregister(self):
        system = System()
        new_org_name = "Org%s" % Base.random_string()
	new_sys_name = "Sys%s" % Base.random_string()
        out,err = system.system_unregister(new_org_name,new_sys_name)
        Assert.equal(err,None)


    def test_system_info(self):
        system = System()
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
	out,err = system.system_info(new_org_name,new_sys_name)
	Assert.equal(err,None)


    def test_system_update(self):
        system = System()
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
        out,err = system.system_update(new_org_name,new_sys_name)
        Assert.equal(err,None)


    def test_system_report(self):
        system = System()
        new_org_name = "Org%s" % Base.random_string()
        out,err = system.system_report(new_org_name)
        Assert.equal(err,None)


    def test_system_subscriptions(self):
        system=System()
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name  = "Sys%s" % Base.random_string()
        out,err = system.system_subscriptions(new_org_name,new_sys_name)
        Assert.equal(err,None)

    
    def test_system_facts(self):
        system = System()
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
        out,err = system.system_facts(new_org_name,new_sys_name)
        Assert.equal(err,None)
      

    def test_system_subscribe(self):
        system = System()
        new_org_name = "Org%s" % Base.random_string()
        new_sys_name = "Sys%s" % Base.random_string()
	new_pool_id = "pool%s" % Base.random_string()
        out,err = system.system_facts(new_org_name,new_sys_name,new_pool_id)
        Assert.equal(err,None)

