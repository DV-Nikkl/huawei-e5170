import requests, hashlib, base64
from bs4 import BeautifulSoup

class Huawei:
    ses_info_url = '/api/webserver/SesTokInfo'
    login_url = '/api/user/login'

    def __init__(self, ip):
        self.ip = ip
        self.session = requests.Session()
        self.getToken()

    def getToken(self):
        r = self.session.get('http://'+self.ip+self.ses_info_url)
        xml = BeautifulSoup(r.text, features="html.parser")
        self.token = xml.response.tokinfo.text
        self.session_id = xml.response.sesinfo.text

    def login(self, user, passw):
        passw = self.encrypt(user, passw)
        headers = {
            '__RequestVerificationToken': self.token,
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Cookie': self.session_id
        }
        xml = '<?xml version="1.0" encoding="UTF-8"?><request><Username>'+user+'</Username><Password>'+passw+'</Password><password_type>4</password_type></request>'
        r = self.session.post('http://'+self.ip+self.login_url, headers=headers, data=xml)
        self.auth_session = r.headers['Set-Cookie']

    def updateHeaders(self):
        self.getToken()
        self.headers = {
            '__RequestVerificationToken': self.token,
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Cookie': self.auth_session
        }

    def encrypt(self, user, passw):
        return self.base64enc(self.sha256(user+self.base64enc(self.sha256(passw))+self.token))

    def sha256(self, s):
        sha_signature = hashlib.sha256(s.encode()).hexdigest()
        return sha_signature

    def base64enc(self, s):
        return base64.b64encode(s.encode()).decode()

# ======= Example Login =======
# huawei = Huawei('192.168.0.1')
# huawei.login('user', 'pass')
