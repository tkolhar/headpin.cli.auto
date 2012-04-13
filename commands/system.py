#!/usr/bin/env python

import subprocess
#from commands.base import Base

class System:
    _command_ = "system"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod    
    def system_list(orgname,u="admin", p="admin"):
	_orgname_flag_ ="--org"
        pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "list", _orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def system_unregister(orgname,sysname,u="admin",p="admin"):
	_orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "unregister", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def system_subscriptions(orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "subscriptions", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def system_subscribe(orgname,sysname,poolid,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
	_poolname_flag_ = "--pool"
        pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "subscribe", _orgname_flag_, orgname, _sysname_flag_, sysname,_poolname_flag_, poolid], stdout=subprocess.PIPE)
        return pout.communicate()             

    @staticmethod
    def system_facts(orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "facts", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def system_update(orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "update", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

 
    @staticmethod
    def system_info(orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "info", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

   
    @staticmethod
    def system_report(orgname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", System._user_flag_, u, System._password_flag_, p, System._command_, "report", _orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
            
