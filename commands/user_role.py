#!/usr/bin/env python

import subprocess
#from commands.base import Base

class User_Role:
    _command_ = "user_role"
    _user_flag_ = "-u"
    _password_flag_ = "-p"
    def user_role_create(self,rolename,u="admin",p="admin"):
        _rolename_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "create", _rolename_flag_, rolename], stdout=subprocess.PIPE)
        return pout.communicate()

    
    def user_role_list(self, u="admin", p="admin"):
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list"], stdout=subprocess.PIPE)
        return pout.communicate()



    def user_role_info(self,name,u="admin",p="admin"):
	_rolename_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "info", _rolename_flag_, name], stdout=subprocess.PIPE)
        return pout.communicate()


    def user_role_update(self,name,u="admin",p="admin"):
	__rolename_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "update", _rolename_flag_, name], stdout=subprocess.PIPE)
        return pout.communicate()


    def user_role_delete(self,name,u="admin",p="admin"):
        _rolename_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "delete",_rolename_flag_, name], stdout=subprocess.PIPE)
        return pout.communicate()
    

          
        
        
        
