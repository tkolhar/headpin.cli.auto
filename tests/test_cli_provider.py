#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.provider import Provider
from commands.base import Base

xfail = pytest.mark.xfail

class TestProvider:
    
    def test_provider_list(self):
        provider = Provider()
 	new_org_name  = "org%s" % Base.random_string()       
        out, err = provider.provider_list(new_org_name)
        Assert.equal(err, None)
        
    def test_provider_info(self):
        provider = Provider()
        new_org_name = "Org%s" % Base.random_string()
	new_provider_name = "provider%s" % Base.random_string()
        out,err = provider.provider_info(new_org_name,new_provider_name)
        Assert.equal(err,None)


    def test_provider_status(self):
        provider = Provider()
        new_org_name = "Org%s" % Base.random_string()
 	new_provider_name = "provider%s" % Base.random_string()
	out,err = provider.provider_status(new_org_name,new_provider_name)
	Assert.equal(err,None)


    def test_provider_import_manifest(self):
        provider = Provider()
        new_org_name = "Org%s" % Base.random_string()
	new_provider_name = "provider%s" % Base.random_string()
        new_file_name = "manifest%s" % Base.random_string() + ".zip"
        out,err = provider.provider_import_manifest(new_org_name,new_provider_name,new_file_name)
        Assert.equal(err,None)
