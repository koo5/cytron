#!/usr/bin/env python
 
from distutils.core import setup
from distutils.extension import Extension
  
setup(name="citron", ext_modules=[Extension("citron", ["citron.cpp"], libraries = ["boost_python"])])
                          