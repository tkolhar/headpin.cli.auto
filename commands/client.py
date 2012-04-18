#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Client:
    _command_ = "client"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod    
    def client_remember(optionname,value,u="admin", p="admin"):
	_optionname_flag_ ="--option"
	_valuename_flag_ = "--value"
        pout = subprocess.Popen(["headpin", Client._user_flag_, u, Client._password_flag_, p,Client._command_, "remember", _optionname_flag_, optionname, _valuename_flag_, value], stdout=subprocess.PIPE)
        return pout.communicate()
 
    @staticmethod
    def client_remember_optionname_missing(value,u="admin", p="admin"):
        _optionname_flag_ ="--option"
        _valuename_flag_ = "--value"
        pout = subprocess.Popen(["headpin", Client._user_flag_, u, Client._password_flag_, p,Client._command_, "remember", _valuename_flag_, value, _optionname_flag_], stderr=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def client_remember_value_missing(optionname,u="admin", p="admin"):
        _optionname_flag_ ="--option"
        _valuename_flag_ = "--value"
        pout = subprocess.Popen(["headpin", Client._user_flag_, u, Client._password_flag_, p,Client._command_, "remember", _optionname_flag_, optionname, _valuename_flag_], stderr=subprocess.PIPE)
        return pout.communicate()


    @staticmethod
    def client_forget(optionname,u="admin",p="admin"):
	_optionname_flag_ = "--option"
	pout = subprocess.Popen(["headpin", Client._user_flag_, u, Client._password_flag_, p, Client._command_, "forget", _optionname_flag_, optionname], stdout=subprocess.PIPE)
        return pout.communicate()

    @staticmethod
    def client_forget_optionname_missing(u="admin",p="admin"):
        _optionname_flag_ = "--option"
        pout = subprocess.Popen(["headpin", Client._user_flag_, u, Client._password_flag_, p, Client._command_, "forget",_optionname_flag_], stderr=subprocess.PIPE)
        return pout.communicate()



    @staticmethod
    def client_saved_options(u="admin",p="admin"):
        pout = subprocess.Popen(["headpin", Client._user_flag_, u, Client._password_flag_, p, Client._command_, "saved_options"], stdout=subprocess.PIPE)
        return pout.communicate()
