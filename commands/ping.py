#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Ping:
    _command_ = "ping"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod    
    def ping_status(u="admin", p="admin"):
        pout = subprocess.Popen(["headpin", Ping._user_flag_, u, Ping._password_flag_, p, Ping._command_], stdout=subprocess.PIPE)
        return pout.communicate()
        
        
        
        
