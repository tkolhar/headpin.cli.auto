#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Product:
    _command_ = "product"
    _user_flag_ = "-u"
    _password_flag_ = "-p"
    
    def product_list(self, orgname,u="admin", p="admin"):
        _orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", self._user_flag_, u, self._password_flag_, p, self._command_,_orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
        
        
        
        
