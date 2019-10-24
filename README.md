# Details
\
__Model:__ Huawei E5170 (compatible with most Huawei E* routers)\
__Firmware version:__ 21.236.17.51.54\
__Webpanel version:__ 14.100.01.11.54

# Usage
\
Connect to router and authenticate
```python
api = Huawei('192.168.0.1')
api.login('username', 'password')
```
\
Request information about connected hosts
```python
hosts = api.listHosts()
```
\
Custom api requests
```python
# GET
response = api.get('/url/to/api', 'optional data')
# POST
response = api.post('/url/to/api', 'optional data')
```
