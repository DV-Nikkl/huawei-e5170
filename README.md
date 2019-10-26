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
__Send custom POST requests__
```python
api.post('/api/led/circle-switch', '<?xml version: "1.0" encoding="UTF-8"?><request><ledSwitch>1</ledSwitch></request>')
```
\
__Send custom GET request__
```python
response = api.get('/api/led/circle-switch')
print(response.text)
```
