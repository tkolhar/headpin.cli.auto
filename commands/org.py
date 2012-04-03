#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Org:
    _command_ = "org"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    def org_create(self,orgname,u="admin",p="admin"):
        _username_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "create", _username_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
    
    def org_list(self, u="admin", p="admin"):
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list"], stdout=subprocess.PIPE)
        return pout.communicate()


    def org_info(self,orgname,u="admin",p="admin"):
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "info", _name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()

    def org_update(self,orgname,u="admin",p="admin"):
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "update", _name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()


    def org_delete(self,orgname,u="admin",p="admin"):
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "delete",_name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
    

    def org_subscriptions(self,orgname,u="admin",p="admin"):
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "delete",_name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()   
        
        
        
        
