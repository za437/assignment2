import unittest
import requests
from bs4 import BeautifulSoup

server_address = "http://127.0.0.1:5000
server_login = server_address + "/login"

def getElementById(text, eid):
    soup = BeautifulSoup(text, "html.parser")
    result = soup.find(id=eid)
    return result
    
class FeatureTest(unittest.TestCase):
    def test_valid_login(self):
    resp = login( "zacisgr8", "54321", "321", "login")
    print("k1")
    print(resp)
    self.assertTrue(resp, "Success! User is logged in")
    
    def test_invalid_login(self):
    resp = login("test", "notpassword" , "none", "Login")
    self.assertFalse(resp, "Invalid Username or Password - Success!")
    
