#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Activation_key:
    _command_ = "activation_key"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod
    def activation_key_create(orgname,name,environment,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_environment_flag_ = "--environment"
	_name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "create", _orgname_flag_, orgname,_name_flag_,name,_environment_flag_, environment], stdout=subprocess.PIPE)
        return pout.communicate()
   
    @staticmethod
    def activation_key_create_orgname_missing(name,environment,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _environment_flag_ = "--environment"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "create", _name_flag_,name,_environment_flag_, environment, _orgname_flag_], stderr=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def activation_key_create_name_missing(orgname,environment,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _environment_flag_ = "--environment"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "create", _orgname_flag_, orgname, _environment_flag_, environment, _name_flag_], stderr=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def activation_key_create_envname_missing(orgname,name,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _environment_flag_ = "--environment"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "create", _orgname_flag_, orgname,_name_flag_,name, _environment_flag_], stderr=subprocess.PIPE)
        return pout.communicate()
 
    @staticmethod
    def activation_key_list(orgname,u="admin", p="admin"):
	_orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "list", _orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def activation_key_list_orgname_missing(u="admin", p="admin"):
        _orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "list", _orgname_flag_], stderr=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def activation_key_info(orgname,name,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "info", _orgname_flag_, orgname,_name_flag_,name], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def activation_key_info_orgname_missing(name,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "info", _name_flag_, name, _orgname_flag_], stderr=subprocess.PIPE)
        return pout.communicate()

  
    @staticmethod
    def activation_key_info_name_missing(orgname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "info", _orgname_flag_, orgname, _name_flag_], stderr=subprocess.PIPE)
        return pout.communicate()



    @staticmethod
    def activation_key_update(orgname,name,u="admin",p="admin"):
	_orgname_flag_ = "--org"
	_name_flag_ = "--name"
	pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u,Activation_key._password_flag_, p, Activation_key._command_, "update", _orgname_flag_, orgname,_name_flag_,name], stdout=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def activation_key_update_orgname_missing(name,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u,Activation_key._password_flag_, p, Activation_key._command_, "update", _name_flag_, name,_orgname_flag_], stderr=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def activation_key_update_name_missing(orgname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u,Activation_key._password_flag_, p, Activation_key._command_, "update", _orgname_flag_, orgname, _name_flag_], stderr=subprocess.PIPE)
        return pout.communicate()



    @staticmethod
    def activation_key_delete(orgname,name,u="admin",p="admin"):
        _orgname_flag_ = "--org"
	_name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "delete",_orgname_flag_, orgname,_name_flag_,name], stdout=subprocess.PIPE)
        return pout.communicate()      


    @staticmethod
    def activation_key_delete_orgname_missing(name,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "delete", _name_flag_, name, _orgname_flag_], stderr=subprocess.PIPE)
        return pout.communicate()


   
    @staticmethod
    def activation_key_delete_name_missing(orgname,u="admin",p="admin"):
        _orgname_flag_ = "--org"
        _name_flag_ = "--name"
        pout = subprocess.Popen(["headpin", Activation_key._user_flag_, u, Activation_key._password_flag_, p, Activation_key._command_, "delete",_orgname_flag_, orgname,_name_flag_], stderr=subprocess.PIPE)
        return pout.communicate()

