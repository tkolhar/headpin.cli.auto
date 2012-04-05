#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Activation_key:
    _command_ = "activation_key"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    def activation_key_create(self,orgname,name,environment,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_environment_flag_ = "--environment"
	_name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "create", _orgname_flag_, orgname,_name_flag_,name,_environment_flag_, environment], stdout=subprocess.PIPE)
        return pout.communicate()
    
    def activation_key_list(self, orgname,u="admin", p="admin"):
	_orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list", _orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()


    def activation_key_info(self,orgname,name,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "info", _orgname_flag_, orgname,_name_flag_,name], stdout=subprocess.PIPE)
        return pout.communicate()

    def activation_key_update(self,orgname,name,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "update", _orgname_flag_, orgname,_name_flag_,name], stdout=subprocess.PIPE)
        return pout.communicate()


    def activation_key_delete(self,orgname,name,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "delete",_orgname_flag_, orgname,_name_flag_,name], stdout=subprocess.PIPE)
        return pout.communicate()      
