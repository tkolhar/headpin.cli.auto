#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.user_role import User_Role
from commands.base import Base

xfail = pytest.mark.xfail

class TestUserRole:
    
    def test_user_role_list(self):
        userrole = User_Role()        
        out, err = userrole.user_role_list()
        Assert.equal(err, None)
        
    def test_user_role_create(self):
        userrole = User_Role()
	new_role_name = "role%s" % Base.random_string()
        out,err = userrole.user_role_create(new_role_name)
        Assert.equal(err,None)


    def test_user_role_info(self):
        userrole = User_Role()
        new_role_name = "role%s" % Base.random_string()
	out,err = userrole.user_role_info(new_role_name)
	Assert.equal(err,None)


    def test_user_role_update(self):
        userrole = User_Role()
        new_role_name = "role%s" % Base.random_string()
        out,err = userrole.user_role_update(new_role_name)
        Assert.equal(err,None)



    def test_user_role_delete(self):
        userrole=User_Role()
        new_role_name = "role%s" % Base.random_string()
        out,err = userrole.user_role_delete(new_role_name)
        Assert.equal(err,None)

