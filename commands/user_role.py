#!/usr/bin/env python

import subprocess
#from commands.base import Base

class User_Role:
    _command_ = "user_role"
    _user_flag_ = "-u"
    _password_flag_ = "-p"
    @staticmethod
    def user_role_create(rolename,u="admin",p="admin"):
        _rolename_flag_ = "--name"
        pout = subprocess.Popen(["headpin", User_Role._user_flag_, u, User_Role._password_flag_, p, User_Role._command_, "create", _rolename_flag_, rolename], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def user_role_list(u="admin", p="admin"):
        pout = subprocess.Popen(["headpin", User_Role._user_flag_, u, User_Role._password_flag_, p, User_Role._command_, "list"], stdout=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def user_role_info(name,u="admin",p="admin"):
	_rolename_flag_ = "--name"
	pout = subprocess.Popen(["headpin", User_Role._user_flag_, u, User_Role._password_flag_, p,User_Role._command_, "info", _rolename_flag_, name], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def user_role_update(name,u="admin",p="admin"):
	_rolename_flag_ = "--name"
	pout = subprocess.Popen(["headpin", User_Role._user_flag_, u, User_Role._password_flag_, p, User_Role._command_, "update", _rolename_flag_, name], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def user_role_delete(name,u="admin",p="admin"):
        _rolename_flag_ = "--name"
        pout = subprocess.Popen(["headpin", User_Role._user_flag_, u, User_Role._password_flag_, p, User_Role._command_, "delete",_rolename_flag_, name], stdout=subprocess.PIPE)
        return pout.communicate()
    

          
        
        
        
