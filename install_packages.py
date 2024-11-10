#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# 설치할 패키지 목록
packages = ['requests', 'Flask']

for package in packages:
    install_package(package)

