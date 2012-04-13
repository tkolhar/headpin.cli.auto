#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.user_role import User_Role
from commands.base import Base

xfail = pytest.mark.xfail

class TestUserRole:
    
    def test_user_role_list(self):
        out, err = User_Role.user_role_list()
        Assert.equal(err, None)
        
    def test_user_role_create(self):
	new_role_name = "role%s" % Base.random_string()
        out,err = User_Role.user_role_create(new_role_name)
        Assert.equal(err,None)


    def test_user_role_info(self):
        new_role_name = "role%s" % Base.random_string()
	out,err = User_Role.user_role_info(new_role_name)
	Assert.equal(err,None)


    def test_user_role_update(self):
        new_role_name = "role%s" % Base.random_string()
        out,err = User_Role.user_role_update(new_role_name)
        Assert.equal(err,None)



    def test_user_role_delete(self):
        new_role_name = "role%s" % Base.random_string()
        out,err = User_Role.user_role_delete(new_role_name)
        Assert.equal(err,None)

