#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.permission import Permission
from commands.base import Base

xfail = pytest.mark.xfail

class TestPermission:
    
    def test_permission_list(self):
        new_user_role = "Role%s" % Base.random_string()       
        out, err = Permission.permission_list(new_user_role)
        Assert.equal(err, None)
        
    def test_permission_create(self):
        new_user_role = "role%s" % Base.random_string()
        new_perm_name = "permission%s" % Base.random_string()
        new_scope_name = "scopename%s" % Base.random_string()
        out,err = Permission.permission_create(new_user_role,new_perm_name,new_scope_name)
        Assert.equal(err,None)


    def test_permission_delete(self):
        new_user_role = "role%s" % Base.random_string()
        new_perm_name = "permission%s" % Base.random_string()
	out,err = Permission.permission_delete(new_user_role,new_perm_name)
	Assert.equal(err,None)


    def test_permission_available_verbs(self):
        out,err = Permission.permission_available_verbs()
        Assert.equal(err,None)
