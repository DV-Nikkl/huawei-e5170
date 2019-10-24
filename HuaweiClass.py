import requests, hashlib, base64
from bs4 import BeautifulSoup

class Huawei:
    # Api urls
    ses_info_url = '/api/webserver/SesTokInfo'
    login_url = '/api/user/login'
    host_list_url = '/api/wlan/host-list'

    def __init__(self, ip):
        self.ip = ip
        self.session = requests.Session()
        self.getToken()

    # return all connected hosts
    def listHosts(self):
        r = self.get(self.host_list_url)
        xml = BeautifulSoup(r.text, features="html.parser")
        hosts = str(xml.response.hosts.text.strip()).replace('\n\n\n', '[HOST]').replace('\n', '[INFO]')
        hosts = hosts.split('[HOST]')

        for i in range(0,len(hosts)):
            hosts[i] = hosts[i].split('[INFO]')

        return hosts

    # custom get/post requests
    def get(self, url, data=''):
        self.updateHeaders()
        if data != '':
            r = self.session.get('http://'+self.ip+url, headers=self.headers, data=data)
        else:
            r = self.session.get('http://'+self.ip+url, headers=self.headers)
        return r

    def post(self, url, data):
        self.updateHeaders()
        if data != '':
            r = self.session.post('http://'+self.ip+url, headers=self.headers, data=data)
        else:
            r = self.session.post('http://'+self.ip+url, headers=self.headers)
        return r

    # request session & token
    def getToken(self):
        r = self.session.get('http://'+self.ip+self.ses_info_url)
        xml = BeautifulSoup(r.text, features="html.parser")
        self.token = xml.response.tokinfo.text
        self.session_id = xml.response.sesinfo.text

    # login using token, session_id, user & pass
    def login(self, user, passw):
        passw = self.encrypt(user, passw)
        headers = {
            '__RequestVerificationToken': self.token,
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': self.session_id
        }
        xml = '<?xml version="1.0" encoding="UTF-8"?><request><Username>'+user+'</Username><Password>'+passw+'</Password><password_type>4</password_type></request>'
        r = self.session.post('http://'+self.ip+self.login_url, headers=headers, data=xml)
        self.auth_session = r.headers['Set-Cookie']

    # generate new token & headers
    def updateHeaders(self):
        self.getToken()
        self.headers = {
            '__RequestVerificationToken': self.token,
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': self.auth_session
        }

    # generate signature from username, password & token
    def encrypt(self, user, passw):
        return self.base64enc(self.sha256(user+self.base64enc(self.sha256(passw))+self.token))

    def sha256(self, s):
        sha_signature = hashlib.sha256(s.encode()).hexdigest()
        return sha_signature

    def base64enc(self, s):
        return base64.b64encode(s.encode()).decode()

# Example api request
huawei = Huawei('192.168.0.1')
huawei.login('admin', 'xs5a3p')
hosts = huawei.listHosts()

print('Clients: '+str(len(hosts)))
