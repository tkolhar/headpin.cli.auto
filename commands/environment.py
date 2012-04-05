#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Environment:
    _command_ = "environment"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    def environment_create(self,orgname,envname,priorenv,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_envname_flag_ = "--name"
	_priorenv_flag_ = "--prior"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "create", _orgname_flag_, orgname,_envname_flag_, envname, _priorenv_flag_, priorenv], stdout=subprocess.PIPE)
        return pout.communicate()
    
    def environment_list(self, orgname,u="admin", p="admin"):
        _orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list", _orgname_flag_,orgname], stdout=subprocess.PIPE)
        return pout.communicate()


    def environment_info(self,orgname,envname,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_envname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "info", _orgname_flag_, orgname,_envname_flag_, envname], stdout=subprocess.PIPE)
        return pout.communicate()

    def environment_update(self,orgname,envname,u="admin",p="admin"):
	_orgname_flag_ = "--org"
        _envname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "update", _orgname_flag_, orgname, _envname_flag_, envname], stdout=subprocess.PIPE)
        return pout.communicate()


    def environment_delete(self,orgname,envname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _envname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "delete",_orgname_flag_, orgname,_envname_flag_, envname], stdout=subprocess.PIPE)
        return pout.communicate()    
