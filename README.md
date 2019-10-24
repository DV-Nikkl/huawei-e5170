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
