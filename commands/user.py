#!/usr/bin/env python

import subprocess
#from commands.base import Base

class User:
    _command_ = "user"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    def user_create(self,username,password,emailid,u="admin",p="admin"):
        _username_flag_ = "--username"
        _password_flag_ = "--password"
        _email_flag_ = "--email"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "create", _username_flag_, username, _password_flag_, password, _email_flag_, emailid], stdout=subprocess.PIPE)
        return pout.communicate()
    
    def user_list(self, u="admin", p="admin"):
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list"], stdout=subprocess.PIPE)
        return pout.communicate()


    def user_info(self,username,u="admin",p="admin"):
	_username_flag_ = "--username"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "info", _username_flag_, username], stdout=subprocess.PIPE)
        return pout.communicate()

    def user_update(self,username,u="admin",p="admin"):
	__username_flag_ = "--username"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "update", _username_flag_, username], stdout=subprocess.PIPE)
        return pout.communicate()
    

   
        
        
        
        
