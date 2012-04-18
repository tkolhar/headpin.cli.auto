#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.provider import Provider
from commands.base import Base

xfail = pytest.mark.xfail

class TestProvider:
    
    def test_provider_list(self):
 	new_org_name  = "org%s" % Base.random_string()       
        out, err = Provider.provider_list(new_org_name)
        Assert.equal(err, None)
 
    def test_provider_list_orgname_missing(self):
        #new_org_name  = "org%s" % Base.random_string()
        out, err = Provider.provider_list_orgname_missing()
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --org option requires an argument\n")

        
    def test_provider_info(self):
        new_org_name = "Org%s" % Base.random_string()
	new_provider_name = "provider%s" % Base.random_string()
        out,err = Provider.provider_info(new_org_name,new_provider_name)
        Assert.equal(err,None)

    def test_provider_info_orgname_missing(self):
        #new_org_name = "Org%s" % Base.random_string()
        new_provider_name = "provider%s" % Base.random_string()
        out,err = Provider.provider_info_orgname_missing(new_provider_name)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --org option requires an argument\n")

    def test_provider_info_providername_missing(self):
        new_org_name = "Org%s" % Base.random_string()
        #new_provider_name = "provider%s" % Base.random_string()
        out,err = Provider.provider_info_providername_missing(new_org_name)
        Assert.equal(err,"Usage: headpin [options]\n\nheadpin: error: --name option requires an argument\n")
 
    def test_provider_status(self):
        new_org_name = "Org%s" % Base.random_string()
 	new_provider_name = "provider%s" % Base.random_string()
	out,err = Provider.provider_status(new_org_name,new_provider_name)
	Assert.equal(err,None)
 

    def test_provider_status_orgname_missing(self):
        #new_org_name = "Org%s" % Base.random_string()
        new_provider_name = "provider%s" % Base.random_string()
        out,err = Provider.provider_status_orgname_missing(new_provider_name)
        Assert.equal(err,None)


    def test_provider_status_providername_missing(self):
        new_org_name = "Org%s" % Base.random_string()
        #new_provider_name = "provider%s" % Base.random_string()
        out,err = Provider.provider_status_providername_missing(new_org_name)
        Assert.equal(err,None)

    def test_provider_import_manifest(self):
        new_org_name = "Org%s" % Base.random_string()
	new_provider_name = "provider%s" % Base.random_string()
        new_file_name = "manifest%s" % Base.random_string() + ".zip"
        out,err = Provider.provider_import_manifest(new_org_name,new_provider_name,new_file_name)
        Assert.equal(err,None)
