import requests, hashlib, base64
from bs4 import BeautifulSoup

class Huawei:
    # Api urls
    api = {
        'ses_info': '/api/webserver/SesTokInfo',
        'login': '/api/user/login',
    }

    # session, token, ip etc.
    router = {
        'ip': '',
        'session': '',
        'token': '',
    }

    def __init__(self, ip):
        self.router['ip'] = ip
        self.session = requests.Session()
        self.getToken()

    # request session & token
    def getToken(self):
        r = self.session.get('http://'+self.router['ip']+self.api['ses_info'])
        xml = BeautifulSoup(r.text, features="html.parser")
        self.router['token'] = xml.response.tokinfo.text
        self.router['session'] = xml.response.sesinfo.text

    # login using token, session, user & pass
    def login(self, user, passw):
        passw = self.encrypt(user, passw)

        headers = {
            '__RequestVerificationToken': self.router['token'],
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': self.router['session']
        }

        xml = '<?xml version="1.0" encoding="UTF-8"?><request><Username>'+user+'</Username><Password>'+passw+'</Password><password_type>4</password_type></request>'
        r = self.session.post('http://'+self.router['ip']+self.api['login'], headers=headers, data=xml)
        self.router['session'] = r.headers['Set-Cookie']

    # generate new token & set headers
    def updateHeaders(self):
        self.getToken()
        self.headers = {
            '__RequestVerificationToken': self.router['token'],
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': self.router['session']
        }

    # custom get/post requests
    def get(self, url, data=''):
        self.updateHeaders()
        if data != '':
            r = self.session.get('http://'+self.router['ip']+url, headers=self.headers, data=data)
        else:
            r = self.session.get('http://'+self.router['ip']+url, headers=self.headers)
        return r

    def post(self, url, data=''):
        self.updateHeaders()
        if data != '':
            r = self.session.post('http://'+self.router['ip']+url, headers=self.headers, data=data)
        else:
            r = self.session.post('http://'+self.router['ip']+url, headers=self.headers)
        return r

    # generate signature from username, password & token
    def encrypt(self, user, passw):
        return self.base64enc(self.sha256(user+self.base64enc(self.sha256(passw))+self.router['token']))

    def sha256(self, s):
        sha_signature = hashlib.sha256(s.encode()).hexdigest()
        return sha_signature

    def base64enc(self, s):
        return base64.b64encode(s.encode()).decode()

