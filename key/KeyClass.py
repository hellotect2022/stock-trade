class KeyClass():
    secret_key = ""
    access_key = ""
    server_url = 'https://api.upbit.com'

    def getSecretKey(self):
        return self.secret_key
    
    def getAccessKey(self):
        return self.access_key

    def getServerUrl(self):
        return self.server_url