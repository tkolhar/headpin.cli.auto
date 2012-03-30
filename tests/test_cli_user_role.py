#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.user_role import User_Role

xfail = pytest.mark.xfail

class TestUserRole:
    
    def test_user_role_list(self):
        userrole = User_Role()        
        out, err = userrole.user_role_list()
        Assert.equal(err, None)
        
    def test_user_role_create(self):
        userrole = User_Role()
        out,err = userrole.user_role_create("rolename")
        Assert.equal(err,None)


    def test_user_role_info(self):
        userrole = User_Role()
	out,err = user.user_role_info("rolename")
	Assert.equal(err,None)


    def test_user_role_update(self):
        userrole = User_Role()
        out,err = user.user_role_update("rolename")
        Assert.equal(err,None)



    def test_user_role_delete(self):
        userrole=User_Role()
        out,err = user.user_role_delete("rolename")
        Assert.equal(err,None)

