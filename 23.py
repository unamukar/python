#!/usr/bin/env python3
class Service:
    lista=[1,2,3]
    def __init__(self,**kwargs):
        self._type=kwargs['type'] if 'type' in kwargs else '"unknown service type"'
        self._app=kwargs['app'] if 'app' in kwargs else '"unknown app"'
        self._version=kwargs['version'] if 'version' in kwargs else '"unknown version"'
    def type(self,t=None):
        if t:self._type=t
        return self._type
    def app(self,a=None):
        if a:self._app=a
        return self._app
    def version(self,v=None):
        if v:self._version=v
        return self._version
    def __str__(self):
        return 'The {} is {} ({})'.format(self.type(),self.app(),self.version())
def main():
    x=Service(type='DNS',app='bind',version='9.11')
    y=Service(type='Web',app='nginx',version='1.13')
    z=Service(type='DB',app='mysql',version='5.5')
    for i in x,y,z:print(i)
    print(Service())
    z.version('5.6');print(z);print(x)
    print(z.lista);z.lista[0]=8;print(z.lista);print(x.lista)
if __name__ == '__main__': main()
