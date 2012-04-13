#!/usr/bin/env python
import pytest
from unittestzero import Assert
from commands.user import User
from commands.base import Base

xfail = pytest.mark.xfail

class TestUser:
    new_user_name = "user%s" % Base.random_string()
    new_password = Base.random_string()
    new_email = new_user_name + "@redhat.com"
    new_role_name = "role%s" % Base.random_string()
     
    
    def test_user_list(self):
        out, err = User.user_list()
        Assert.equal(err, None)
        
    def test_user_create(self):
        out,err = User.user_create(self.new_user_name,self.new_password,self.new_email)
        Assert.equal(err,None)


    def test_user_info(self):
	out,err = User.user_info(self.new_user_name)
	Assert.equal(err,None)


    def test_user_update(self):
        out,err = User.user_update(self.new_user_name)
        Assert.equal(err,None)

    def test_user_report(self):
        out, err = User.user_report(self.new_user_name)
        Assert.equal(err, None) 


    def test_user_assign_role(self):
	out,err = User.user_assign_role(self.new_user_name,self.new_role_name)
        Assert.equal(err,None) 
   

    def test_user_unassign_role(self):
        out,err = User.user_unassign_role(self.new_user_name,self.new_role_name)
        Assert.equal(err,None)


    def test_user_list_roles(self):
        out,err = User.user_list_roles(self.new_role_name)
        Assert.equal(err,None)


    def test_user_delete(self):
        out,err = User.user_delete("samplename")
        Assert.equal(err,None)

