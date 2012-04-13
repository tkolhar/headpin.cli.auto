#!/usr/bin/env python

import subprocess
#from commands.base import Base

class Product:
    _command_ = "product"
    _user_flag_ = "-u"
    _password_flag_ = "-p"

    @staticmethod    
    def product_list(orgname,u="admin", p="admin"):
        _orgname_flag_ = "--org"
        pout = subprocess.Popen(["headpin", Product._user_flag_, u, Product._password_flag_, p, Product._command_,_orgname_flag_, orgname], stdout=subprocess.PIPE)
        return pout.communicate()
        
        
        
        
