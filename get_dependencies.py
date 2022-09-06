# -*- coding: utf-8 -*-
"""
Created on Mon Sep 06 11:51 2022

@author: https://github.com/erickorsi

Script for downloading dependencies of the polyglot package.
"""
import os
import sys
import requests

#--------------------------------------------------------------------------------
def get_wheels(pyicu_version="2.9", pycld2_version="0.41"):
    '''
    Downloads the required wheels from https://www.lfd.uci.edu/~gohlke/pythonlibs/
    according to the interpreter Python version.

    Wheels Morfessor and futures are already downloaded, and work for any Python 3 version.

    Parameters
    ----------
    pyicu_version : string, default="2.9"
        Which version of the PyICU wheel you want to download.
    pycld2_version : string, default="0.41"
        Which version of the pycld2 wheel you want to download.

    Returns
    ----------
    None.
    May raise error in case of unsupported python version, wrong wheel version, or connection error.
    Saves the wheels PyICU and pycld2 in the wheels forlder, located in the same directory as this script.
    '''
    # Versions
    v = sys.version_info
    if v.major == 2:
        print("Only supported for python 3.")
        raise SystemExit
    v1 = str(v.major) + str(v.minor)
    print("Python version {maj}.{min}.{mic}".format(maj=v.major,min=v.minor,mic=v.micro))
    if sys.maxsize > 2**32:
        v2 = "_amd64"
        print("Running on 64bit processor.")
    else:
        v2 = "32"
        print("Running on 32bit processor.")

    # PyICU
    print("Downloading wheel PyICU-{0}".format(pyicu_version))
    try:
        wheel = "PyICU-{pyicu}-cp{v1}-cp{v1}-win{v2}.whl".format(pyicu=pyicu_version,v1=v1,v2=v2)
        response = requests.get(url = "https://download.lfd.uci.edu/pythonlibs/archived/"+wheel)
        open(os.path.join(dir_path, wheel), "wb").write(response.content)
        print("PyICU-{0} downloaded.".format(pyicu_version))
    except Exception as e:
        print("Unable to download PyICU:\n", e)
        raise SystemExit

    # pycld2
    print("Downloading wheel pycld2-{0}".format(pycld2_version))
    try:
        wheel = "pycld2-{pycld2}-cp{v1}-cp{v1}-win{v2}.whl".format(pycld2=pycld2_version,v1=v1,v2=v2)
        response = requests.get(url = "https://download.lfd.uci.edu/pythonlibs/archived/"+wheel)
        open(os.path.join(dir_path, wheel), "wb").write(response.content)
    except Exception as e:
        print("Unable to download pycld2:\n", e)
        raise SystemExit

def install_wheels():
    '''
    Installs the downloaded wheels.

    Parameters
    ----------
    None.

    Returns
    ----------
    None.
    May raise error if unable to install.
    '''
    for wheel in dir_path.listdir():
        if wheel.endwith(".whl"):
            print("Installing "+ wheel +"...")
            try:
                os.system('python -m pip install '+ wheel)
                print("Wheel installed.")
            except Exception as e:
                print("Unable to install wheel:\n", e)
                raise SystemExit

#--------------------------------------------------------------------------------
# Wheels directory
dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wheels")
print("Wheels folder:", dir_path)
get_wheels()
install_wheels()