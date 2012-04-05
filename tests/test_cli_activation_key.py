#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.activation_key import Activation_key
from commands.base import Base

xfail = pytest.mark.xfail

class TestOrg:
    
    def test_activation_key_list(self):
        activation_key = Activation_key()       
	base = Base()
	new_org_name = "org%s" % base.random_string()
        out, err = activation_key.activation_key_list(new_org_name)
        Assert.equal(err, None)
        
    def test_activation_key_create(self):
        activation_key = Activation_key()
        base = Base()
        new_org_name = "Org%s" % base.random_string()
        new_env_name = "Env%s" % base.random_string()
	new_activation_key = "act%s" % base.random_string()
        out,err = activation_key.activation_key_create(new_org_name,new_activation_key,new_env_name)
        Assert.equal(err,None)


    def test_activation_key_info(self):
        activation_key = Activation_key()
	base = Base()
        new_org_name = "Org%s" % base.random_string()
	new_activation_key = "act%s" % base.random_string()
	out,err = activation_key.activation_key_info(new_org_name,new_activation_key)
	Assert.equal(err,None)


    def test_activation_key_update(self):
        activation_key = Activation_key()
	base = Base()
        new_org_name = "Org%s" % base.random_string()
	new_activation_key = "act%s" % base.random_string()
        out,err = activation_key.activation_key_update(new_org_name,new_activation_key)
        Assert.equal(err,None)


    def test_activation_key_delete(self):
        activation_key =  Activation_key()
	base = Base()
        new_org_name = "Org%s" % base.random_string()
	new_activation_key = "act%s" % base.random_string()
        out,err = activation_key.activation_key_delete(new_org_name,new_activation_key)
        Assert.equal(err,None)
