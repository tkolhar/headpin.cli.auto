#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Client:
    _command_ = "client"
    _user_flag_ = "-u"
    _password_flag_ = "-p"
    
    def client_remember(self, optionname,value,u="admin", p="admin"):
	_optionname_flag_ ="--option"
	_valuename_flag_ = "--value"
	
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "remember", _optionname_flag_, optionname, _valuename_flag_, value], stdout=subprocess.PIPE)
        return pout.communicate()

    def client_forget(self,optionname,value,u="admin",p="admin"):
	_optionname_flag_ = "--option"
	_valuename_flag_ = "--value"
        print optionname + "\n"
        print value + "\n"
	pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "forget", _optionname_flag_, optionname, _valuename_flag_, value], stdout=subprocess.PIPE)
        return pout.communicate()


    def client_saved_options(self,u="admin",p="admin"):
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_, "saved_options"], stdout=subprocess.PIPE)
        return pout.communicate()
