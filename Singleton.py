'''
Challange:
Create a way to set and get configuration settings for an internet server using the Singleton Design Pattern
'''

class SingletonConfigurationManager:

    __instance = None
    network_configuration = {}

    def getInstance():
        if SingletonConfigurationManager.__instance == None:
            SingletonConfigurationManager()
        return SingletonConfigurationManager.__instance
    
    def __init__(self):
        if SingletonConfigurationManager.__instance != None:
            raise Exception("Instance is already created")
        else:
            SingletonConfigurationManager.__instance = self

    def setConfiguration(self,key,value):
        self.network_configuration[key] = value
            
    def getConfiguration(self,key):
        return self.network_configuration[key]

s1 = SingletonConfigurationManager.getInstance()
s2 = SingletonConfigurationManager.getInstance()

s1.setConfiguration('ip_address','192.168.1.1')
s2.setConfiguration('proxy_server','100.0.0.1')
s2.setConfiguration('ip_version','IPv4')

print('ip_address:', s2.getConfiguration('ip_address'))