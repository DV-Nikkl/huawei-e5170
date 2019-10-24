from src.HuaweiClass import Huawei

# Authenticate
huawei = Huawei('192.168.0.1')
huawei.login('username', 'password')

# Api requests
hosts = huawei.listHosts()
print('Clients: '+str(len(hosts)))

# Print device information
huawei.deviceInfo()
