# Details
\
__Model:__ Huawei E5170s-22 (compatible with most Huawei E* routers)\
__Firmware version:__ 21.236.17.51.54\
__WebUI version:__ 14.100.01.11.54

# Usage
\
__Connect to router and authenticate__
```python
api = Huawei('192.168.0.1')
api.login('username', 'password')
```
\
__Print device information__
```python
api.deviceInfo()
```
\
__Return list of connected hosts__
```python
hosts = api.listHosts()
```
\
__Send custom api requests (XML response)__
```python
# IMPORTANT: Request new token
api.updateHeaders()

# GET
response = api.get('/url/to/api', 'optional data')
# POST
response = api.post('/url/to/api', 'optional data')
```
