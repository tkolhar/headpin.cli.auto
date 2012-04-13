#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Org:
    _command_ = "org"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod
    def org_create(orgname,u="admin",p="admin"):
        _orgname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Org._user_flag_, u, Org._password_flag_, p, Org._command_, "create", _orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
    
    @staticmethod
    def org_list(u="admin", p="admin"):
        pout = subprocess.Popen(["headpin", Org._user_flag_, u, Org._password_flag_, p, Org._command_, "list"], stdout=subprocess.PIPE)
        return pout.communicate()

     
    @staticmethod
    def org_info(orgname,u="admin",p="admin"):
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Org._user_flag_, u, Org._password_flag_, p, Org._command_, "info", _name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def org_update(orgname,u="admin",p="admin"):
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Org._user_flag_, u, Org._password_flag_, p, Org._command_, "update", _name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def org_delete(orgname,u="admin",p="admin"):
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Org._user_flag_, u, Org._password_flag_, p, Org._command_, "delete",_name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
    
    @staticmethod
    def org_subscriptions(orgname,u="admin",p="admin"):
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Org._user_flag_, u, Org._password_flag_, p, Org._command_, "delete",_name_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()   
        
        
        
        
