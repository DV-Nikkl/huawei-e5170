# Details
\
__Model:__ Huawei E5170s-22 (compatible with most Huawei E* routers)\
__Firmware version:__ 21.236.17.51.54\
__WebUI version:__ 14.100.01.11.54

# Usage
\
Connect to router and authenticate
```python
api = Huawei('192.168.0.1')
api.login('username', 'password')
```
\
Print device information
```python
api.deviceInfo()
```
\
Return list of connected hosts
```python
hosts = api.listHosts()
```
\
Send custom api requests
```python
api.updateHeaders() # IMPORTANT: Request new token

# GET
response = api.get('/url/to/api', 'optional data')
# POST
response = api.post('/url/to/api', 'optional data')
```
\
