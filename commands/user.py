#!/usr/bin/env python

import subprocess
#from commands.base import Base

class User:
    _command_ = "user"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod
    def user_create(username,password,emailid,u="admin",p="admin"):
        _username_flag_ = "--username"
        _password_flag_ = "--password"
        _email_flag_ = "--email"
        pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "create", _username_flag_, username, _password_flag_, password, _email_flag_, emailid], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod    
    def user_list(u="admin", p="admin"):
        pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "list"], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def user_info(username,u="admin",p="admin"):
	_username_flag_ = "--username"
	pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "info", _username_flag_, username], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def user_update(username,u="admin",p="admin"):
	_username_flag_ = "--username"
	pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "update", _username_flag_, username], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def user_report(username,u="admin",p="admin"):
	_username_flag_ = "--username"
        pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "report", _username_flag_, username], stdout=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def user_assign_role(username,role,u="admin",p="admin"):
        _username_flag_ = "--username"
        _role_flag_ = "--role"
        pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "assign_role", _username_flag_, username, _role_flag_, role], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def user_unassign_role(username,role,u="admin",p="admin"):
        _username_flag_ = "--username"
        _role_flag_ = "--role"
        pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "unassign_role", _username_flag_, username, _role_flag_, role], stdout=subprocess.PIPE)
        return pout.communicate()
   
    @staticmethod
    def user_list_roles(username,u="admin",p="admin"):
        _username_flag_ = "--username"
        pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "list_roles",_username_flag_, username], stdout=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def user_delete(username,u="admin",p="admin"):
        _username_flag_ = "--username"
        pout = subprocess.Popen(["headpin", User._user_flag_, u, User._password_flag_, p, User._command_, "delete",_username_flag_, username], stdout=subprocess.PIPE)
        return pout.communicate()
    

   
        
        
        
        
