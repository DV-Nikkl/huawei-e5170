from src.HuaweiClass import Huawei

# Authenticate
api = Huawei('192.168.0.1')
api.login('username', 'password')

# Custom POST request to turn led on
api.post('/api/led/circle-switch', '<?xml version: "1.0" encoding="UTF-8"?><request><ledSwitch>1</ledSwitch></request>')

# Custom GET request to get led status
response = api.get('/api/led/circle-switch')
print(response.text)
