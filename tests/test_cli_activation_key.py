#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.activation_key import Activation_key
from commands.base import Base

xfail = pytest.mark.xfail

class TestOrg:
    
    def test_activation_key_list(self):
	new_org_name = "org%s" % Base.random_string()
        out, err = Activation_key.activation_key_list(new_org_name)
        Assert.equal(err, None)
     
    def test_activation_key_list_orgname_missing(self):
        #new_org_name = "org%s" % Base.random_string()
        out, err = Activation_key.activation_key_list_orgname_missing()
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --org option requires an argument\n")
   
    def test_activation_key_create(self):
        new_org_name = "Org%s" % Base.random_string()
        new_env_name = "Env%s" % Base.random_string()
	new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_create(new_org_name,new_activation_key,new_env_name)
        Assert.equal(err,None)

    
    def test_activation_key_create_orgname_missing(self):
        #new_org_name = "Org%s" % Base.random_string()
        new_env_name = "Env%s" % Base.random_string()
        new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_create_orgname_missing(new_activation_key,new_env_name)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --org option requires an argument\n")
   
    def test_activation_key_create_name_missing(self):
        new_org_name = "Org%s" % Base.random_string()
        new_env_name = "Env%s" % Base.random_string()
        #new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_create_name_missing(new_org_name,new_env_name)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --name option requires an argument\n")

    def test_activation_key_create_envname_missing(self):
        new_org_name = "Org%s" % Base.random_string()
        #new_env_name = "Env%s" % Base.random_string()
        new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_create_envname_missing(new_org_name,new_activation_key)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --environment option requires an argument\n")

    def test_activation_key_info(self):
        new_org_name = "Org%s" % Base.random_string()
	new_activation_key = "act%s" % Base.random_string()
	out,err = Activation_key.activation_key_info(new_org_name,new_activation_key)
	Assert.equal(err,None)


    def test_activation_key_info_orgname_missing(self):
        #new_org_name = "Org%s" % Base.random_string()
        new_activate_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_info_orgname_missing(new_activate_key)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --org option requires an argument\n")


    def test_activation_key_info_name_missing(self):
        new_org_name = "Org%s" % Base.random_string()
        #new_activate_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_info_name_missing(new_org_name)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --name option requires an argument\n")


    def test_activation_key_update(self):
        new_org_name = "Org%s" % Base.random_string()
	new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_update(new_org_name,new_activation_key)
        Assert.equal(err,None)

    def test_activation_key_update_orgname_missing(self):
        #new_org_name = "Org%s" % Base.random_string()
        new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_update_orgname_missing(new_activation_key)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --org option requires an argument\n")

    def test_activation_key_update_name_missing(self):
        new_org_name = "Org%s" % Base.random_string()
        #new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_update_name_missing(new_org_name)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --name option requires an argument\n")


    def test_activation_key_delete(self):
        new_org_name = "Org%s" % Base.random_string()
	new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_delete(new_org_name,new_activation_key)
        Assert.equal(err,None)


    def test_activation_key_delete_orgname_missing(self):
        #new_org_name = "Org%s" % Base.random_string()
        new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_delete_orgname_missing(new_activation_key)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --org option requires an argument\n")

 
    def test_activation_key_delete_name_missing(self):
        new_org_name = "Org%s" % Base.random_string()
        #new_activation_key = "act%s" % Base.random_string()
        out,err = Activation_key.activation_key_delete_name_missing(new_org_name)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --name option requires an argument\n")

