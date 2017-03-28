from nose.tools import *

#run nosetests in above folder
def setup():
    print ("SETUP!")

def tearDown():
    print("TEAR DOWN")

def test_basic():
    print("TEST BASIC RAN")