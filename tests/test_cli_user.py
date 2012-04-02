#!/usr/bin/env python
import pytest
from unittestzero import Assert
from commands.user import User
from commands.base import Base

xfail = pytest.mark.xfail

class TestUser:
    base = Base()
    new_user_name = "user%s" % base.random_string()
    new_password = base.random_string()
    new_email = new_user_name + "@redhat.com"
    new_role_name = "role%s" % base.random_string()
     
    
    def test_user_list(self):
        user = User()        
        out, err = user.user_list()
        Assert.equal(err, None)
        
    def test_user_create(self):
        user = User()
        #base = Base()
        #new_user_name = "user%s" % base.random_string()
	#new_password = base.random_string()
	#new_email = new_user_name + "@redhat.com"
        out,err = user.user_create(self.new_user_name,self.new_password,self.new_email)
        Assert.equal(err,None)


    def test_user_info(self):
        user = User()
	#base = Base()
        #new_user_name = "user%s" % base.random_string()
	out,err = user.user_info(self.new_user_name)
	Assert.equal(err,None)


    def test_user_update(self):
        user = User()
	#base = Base()
        #new_user_name = "user%s" % base.random_string()
        out,err = user.user_update(self.new_user_name)
        Assert.equal(err,None)

    def test_user_report(self):
        user = User()
	#base = Base()
        #new_user_name = "user%s" % base.random_string()
        out, err = user.user_report(self.new_user_name)
        Assert.equal(err, None) 


    def test_user_assign_role(self):
        user=User()
	#base = Base()
        #new_user_name = "user%s" % base.random_string()
	#new_role_name = "role%s" % base.random_string()
	out,err = user.user_assign_role(self.new_user_name,self.new_role_name)
        Assert.equal(err,None) 
   

    def test_user_unassign_role(self):
        user=User()
	#base = Base()
        #new_user_name = "user%s" % base.random_string()
        #new_role_name = "role%s" % base.random_string()
        out,err = user.user_unassign_role(self.new_user_name,self.new_role_name)
        Assert.equal(err,None)


    def test_user_list_roles(self):
        user=User()
	#base = Base()
        #new_role_name = "role%s" % base.random_string()
        out,err = user.user_list_roles(self.new_role_name)
        Assert.equal(err,None)


    def test_user_delete(self):
        user=User()
        out,err = user.user_delete("samplename")
        Assert.equal(err,None)

