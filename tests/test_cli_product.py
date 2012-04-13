#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.product import Product
from commands.base import Base

xfail = pytest.mark.xfail

class TestProduct:
    
    def test_product_list(self):
        orgname = "Org%s" % Base.random_string()
        out, err = Product.product_list(orgname)
        Assert.equal(err, None)
        
