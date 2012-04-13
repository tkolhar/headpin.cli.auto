#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Environment:
    _command_ = "environment"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod
    def environment_create(orgname,envname,priorenv,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_envname_flag_ = "--name"
	_priorenv_flag_ = "--prior"
        pout = subprocess.Popen(["headpin", Environment._user_flag_, u, Environment._password_flag_, p, Environment._command_, "create", _orgname_flag_, orgname,_envname_flag_, envname, _priorenv_flag_, priorenv], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def environment_list(orgname,u="admin", p="admin"):
        _orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", Environment._user_flag_, u, Environment._password_flag_, p, Environment._command_, "list", _orgname_flag_,orgname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod  
    def environment_info(orgname,envname,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_envname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Environment._user_flag_, u, Environment._password_flag_, p, Environment._command_, "info", _orgname_flag_, orgname,_envname_flag_, envname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def environment_update(orgname,envname,u="admin",p="admin"):
	_orgname_flag_ = "--org"
        _envname_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Environment._user_flag_, u, Environment._password_flag_, p, Environment._command_, "update", _orgname_flag_, orgname, _envname_flag_, envname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def environment_delete(orgname,envname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _envname_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Environment._user_flag_, u, Environment._password_flag_, p, Environment._command_, "delete",_orgname_flag_, orgname,_envname_flag_, envname], stdout=subprocess.PIPE)
        return pout.communicate()    
