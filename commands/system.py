#!/usr/bin/env python

import subprocess
#from commands.base import Base

class System:
    _command_ = "system"
    _user_flag_ = "-u"
    _password_flag_ = "-p"
    
    def system_list(self, orgname,u="admin", p="admin"):
	_orgname_flag_ ="--org"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list", _orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()


    def system_unregister(self,orgname,sysname,u="admin",p="admin"):
	_orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "unregister", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

    def system_subscriptions(self,orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "subscriptions", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

    def system_subscribe(self,orgname,sysname,poolid,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
	_poolname_flag_ = "--pool"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "subscribe", _orgname_flag_, orgname, _sysname_flag_, sysname,_poolname_flag_, poolid], stdout=subprocess.PIPE)
        return pout.communicate()             

    def system_facts(self,orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "facts", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()


    def system_update(self,orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "update", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

 
    def system_info(self,orgname,sysname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _sysname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "info", _orgname_flag_, orgname, _sysname_flag_, sysname], stdout=subprocess.PIPE)
        return pout.communicate()

   
    def system_report(self,orgname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "report", _orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
            
