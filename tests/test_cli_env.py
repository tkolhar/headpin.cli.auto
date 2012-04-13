#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.environment import Environment
from commands.base import Base

xfail = pytest.mark.xfail

class TestEnv:
    
    def test_env_list(self):
	new_org_name = "Org%s" % Base.random_string() 
        out, err = Environment.environment_list(new_org_name)
        Assert.equal(err, None)
        
    def test_env_create(self):
        new_env_name = "Env%s" % Base.random_string()
        new_org_name = "Org%s" % Base.random_string()
        new_env_prior = "Prior%s" % Base.random_string()
        out,err = Environment.environment_create(new_org_name,new_env_name,new_env_prior)
        Assert.equal(err,None)


    def test_env_info(self):
        new_org_name = "Org%s" % Base.random_string()
	new_env_name = "Env%s" % Base.random_string()
	out,err = Environment.environment_info(new_org_name,new_env_name)
	Assert.equal(err,None)


    def test_env_update(self):
        new_org_name = "Org%s" % Base.random_string()
        new_env_name = "Env%s" % Base.random_string()
        out,err =Environment.environment_update(new_org_name,new_env_name)
        Assert.equal(err,None)


    def test_env_delete(self):
	new_org_name = "Org%s" % Base.random_string()
        new_env_name = "Env%s" % Base.random_string()
        out,err = Environment.environment_delete(new_org_name,new_env_name)
        Assert.equal(err,None)
