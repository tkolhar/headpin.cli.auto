#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Provider:
    _command_ = "provider"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    
    def provider_list(self, orgname,u="admin", p="admin"):
	_orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list","_orgname_flag_",orgname], stdout=subprocess.PIPE)
        return pout.communicate()


    def provider_info(self,orgname,providername,u="admin",p="admin"):
	_orgname_flag_ = "--org"
        _provider_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "info", _orgname_flag_, orgname,_provider_flag_,providername], stdout=subprocess.PIPE)
        return pout.communicate()

    def provider_status(self,orgname,providername,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_provider_flag_ = "--name"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "status", _orgname_flag_, orgname,_provider_flag_,providername], stdout=subprocess.PIPE)
        return pout.communicate()


    def provider_import_manifest(self,orgname,providername,file,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_provider_flag_ = "--name"
	_file_flag_ = "--file"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "import_manifest",_orgname_flag_, orgname,_provider_flag_,providername,_file_flag_, file], stdout=subprocess.PIPE)
        return pout.communicate()
