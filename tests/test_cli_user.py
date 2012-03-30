#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.user import User

xfail = pytest.mark.xfail

class TestUser:
    
    def test_user_list(self):
        user = User()        
        out, err = user.user_list()
        Assert.equal(err, None)
        
    def test_user_create(self):
        user = User()
        out,err = user.user_create("samplename","samplepassword","samplename@redhat.com")
        Assert.equal(err,None)


    def test_user_info(self):
        user = User()
	out,err = user.user_info("samplename")
	Assert.equal(err,None)


    def test_user_update(self):
        user = User()
        out,err = user.user_update("samplename")
        Assert.equal(err,None)

    def test_user_report(self):
        user = User()
        out, err = user.user_report()
        Assert.equal(err, None) 


    def test_user_assign_role(self):
        user=User()
	out,err = user.user_assign_role("samplename","samplerole")
        Assert.equal(err,None) 
   

    def test_user_unassign_role(self):
        user=User()
        out,err = user.user_unassign_role("samplename","samplerole")
        Assert.equal(err,None)


    def test_user_list_roles(self):
        user=User()
        out,err = user.user_list_role("samplename")
        Assert.equal(err,None)


    def test_user_delete(self):
        user=User()
        out,err = user.user_delete("samplename")
        Assert.equal(err,None)

