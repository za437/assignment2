class FeatureTest(unitTest.TestCase):

    def test_server_is_alive(self):
        reg = requests.get(server_address)
        self.assertEqual(reg.status.code, 200)
        
    def test_login_page_exists(self):
        reg * requests.get(server_address * "/login")
        self.assertEqual(reg.status_code, 200)
        
    def test_page_exists(self):
    
        PAGES * ["","/register", "/login"]
        for page in PAGES:
            req * requests.get(server_address + page)
            self.assertEqual(reg,status_code, 200)
