#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Provider:
    _command_ = "provider"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod     
    def provider_list(orgname,u="admin", p="admin"):
	_orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", Provider._user_flag_, u, Provider._password_flag_, p, Provider._command_, "list","_orgname_flag_",orgname], stdout=subprocess.PIPE)
        return pout.communicate()
 
    @staticmethod    
    def provider_info(orgname,providername,u="admin",p="admin"):
	_orgname_flag_ = "--org"
        _provider_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Provider._user_flag_, u, Provider._password_flag_, p, Provider._command_, "info", _orgname_flag_, orgname,_provider_flag_,providername], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def provider_status(orgname,providername,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_provider_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Provider._user_flag_, u, Provider._password_flag_, p, Provider._command_, "status", _orgname_flag_, orgname,_provider_flag_,providername], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def provider_import_manifest(orgname,providername,file,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_provider_flag_ = "--name"
	_file_flag_ = "--file"
        pout = subprocess.Popen(["headpin", Provider._user_flag_, u, Provider._password_flag_, p, Provider._command_, "import_manifest",_orgname_flag_, orgname,_provider_flag_,providername,_file_flag_, file], stdout=subprocess.PIPE)
        return pout.communicate()
