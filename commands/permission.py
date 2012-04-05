#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Permission:
    _command_ = "permission"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    def permission_create(self,user_role,perm_name,scopename,u="admin",p="admin"):
        _userrole_flag_ = "--user_role"
        _perm_name_flag_ = "--name"
        _scope_flag_ = "--scope"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "create", _userrole_flag_, user_role,_perm_name_flag_,perm_name,_scope_flag_, scopename], stdout=subprocess.PIPE)
        return pout.communicate()
    
    def permission_list(self, user_role,u="admin", p="admin"):
        _userrole_flag_ = "--user_role"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "list", _userrole_flag_, user_role], stdout=subprocess.PIPE)
        return pout.communicate()


    def permission_delete(self,user_role,perm_name,u="admin",p="admin"):
        _userrole_flag_ = "--user_role"
        _perm_name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "delete",_userrole_flag_, user_role,_perm_name_flag_, perm_name], stdout=subprocess.PIPE)
        return pout.communicate()
    

    def permission_available_verbs(self,u="admin",p="admin"):
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "available_verbs"], stdout=subprocess.PIPE)
        return pout.communicate()   
        
        
        
        
