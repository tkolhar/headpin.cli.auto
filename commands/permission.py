#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Permission:
    _command_ = "permission"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod
    def permission_create(user_role,perm_name,scopename,u="admin",p="admin"):
        _userrole_flag_ = "--user_role"
        _perm_name_flag_ = "--name"
        _scope_flag_ = "--scope"
        pout = subprocess.Popen(["headpin", Permission._user_flag_, u, Permission._password_flag_, p, Permission._command_, "create", _userrole_flag_, user_role,_perm_name_flag_,perm_name,_scope_flag_, scopename], stdout=subprocess.PIPE)
        return pout.communicate()
    
    @staticmethod
    def permission_list(user_role,u="admin", p="admin"):
        _userrole_flag_ = "--user_role"
        pout = subprocess.Popen(["headpin", Permission._user_flag_, u, Permission._password_flag_, p, Permission._command_, "list", _userrole_flag_, user_role], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def permission_delete(user_role,perm_name,u="admin",p="admin"):
        _userrole_flag_ = "--user_role"
        _perm_name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Permission._user_flag_, u, Permission._password_flag_, p, Permission._command_, "delete",_userrole_flag_, user_role,_perm_name_flag_, perm_name], stdout=subprocess.PIPE)
        return pout.communicate()
    
    @staticmethod
    def permission_available_verbs(u="admin",p="admin"):
        pout = subprocess.Popen(["headpin", Permission._user_flag_, u, Permission._password_flag_, p, Permission._command_, "available_verbs"], stdout=subprocess.PIPE)
        return pout.communicate()   
        
        
        
        
