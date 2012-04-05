#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.environment import Environment
from commands.base import Base

xfail = pytest.mark.xfail

class TestEnv:
    
    def test_env_list(self):
        env =Environment()      
	base = Base()
	new_org_name = "Org%s" % base.random_string() 
        out, err = env.environment_list(new_org_name)
        Assert.equal(err, None)
        
    def test_env_create(self):
        env = Environment()
        base = Base()
        new_env_name = "Env%s" % base.random_string()
        new_org_name = "Org%s" % base.random_string()
        new_env_prior = "Prior%s" % base.random_string()
        out,err = env.environment_create(new_org_name,new_env_name,new_env_prior)
        Assert.equal(err,None)


    def test_env_info(self):
        env =Environment()
	base = Base()
        new_org_name = "Org%s" % base.random_string()
	new_env_name = "Env%s" % base.random_string()
	out,err = env.environment_info(new_org_name,new_env_name)
	Assert.equal(err,None)


    def test_env_update(self):
        env = Environment()
	base = Base()
        new_org_name = "Org%s" % base.random_string()
        new_env_name = "Env%s" % base.random_string()
        out,err = env.environment_update(new_org_name,new_env_name)
        Assert.equal(err,None)


    def test_env_delete(self):
        env=Environment()
	base = Base()
        new_org_name = "Org%s" % base.random_string()
        new_env_name = "Env%s" % base.random_string()
        out,err = env.environment_delete(new_org_name,new_env_name)
        Assert.equal(err,None)
