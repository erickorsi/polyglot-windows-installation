# -*- coding: utf-8 -*-
"""
Created on Mon Sep 06 11:51 2022

@author: https://github.com/erickorsi

Script for downloading dependencies of the polyglot package.
"""

import sys
import requests

response = requests.get(url = "https://www.lfd.uci.edu/~gohlke/pythonlibs",
                           headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
                           })

